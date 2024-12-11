from flask import Flask, render_template, request, jsonify, session
from sentiment_analysis import analyze_sentiment
from query_processing import clean_query
from rag_agent import query_rag
from response_assembly_agent import assemble_response
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default_key_for_dev")

@app.route("/")
def home():
    """Render the homepage."""
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def handle_query():
    """Handle single queries for sentiment analysis."""
    user_input = request.json.get("query", "").strip()

    # Basic validation
    if not user_input:
        return jsonify({"error": "Query cannot be empty."}), 400
    if len(user_input) > 512:
        return jsonify({"error": "Query is too long. Please limit to 512 characters."}), 400

    # Clean the query
    cleaned_query = clean_query(user_input)

    # Perform sentiment analysis
    sentiment_result = analyze_sentiment(cleaned_query)

    # Return the cleaned query and sentiment analysis result
    response = {
        "cleaned_query": cleaned_query,
        "sentiment": sentiment_result["label"],
        "confidence": sentiment_result["score"]
    }
    return jsonify(response)

@app.route("/combined", methods=["POST"])
def combined():
    """Handle combined queries for RAG + Sentiment Analysis."""
    user_query = request.form["combined_query"]

    try:
        # Get the RAG output
        rag_result = query_rag(user_query)

        # Perform sentiment analysis
        sentiment_result = analyze_sentiment(user_query)

        # Assemble the final response
        response = assemble_response(user_query, rag_result, sentiment_result)

        # Render the results in a user-friendly format
        return render_template(
            "results.html",
            query=user_query,
            rag_result=rag_result,
            sentiment_result=sentiment_result,
            final_response=response,
        )

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route("/chat", methods=["POST", "GET"])
def chat():
    """
    Handle user queries dynamically with sentiment analysis and RAG.
    """
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_query = request.form["user_query"]

        # Perform sentiment analysis
        sentiment_result = analyze_sentiment(user_query)

        # Fetch relevant product info using the RAG agent
        product_info = query_rag(user_query)

        # Assemble a tailored response
        response = assemble_response(user_query, product_info, sentiment_result)

        # Update chat history
        session["chat_history"].append({"sender": "User", "text": user_query})
        session["chat_history"].append({"sender": "Chatbot", "text": response})

    # Render the chat interface
    return render_template("index.html", chat_history=session["chat_history"])


if __name__ == "__main__":
    app.run(debug=True)
