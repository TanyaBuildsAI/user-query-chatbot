from query_processing import clean_query
from flask import Flask, render_template, request, jsonify
from transformers import pipeline


# Initialize Flask app
app = Flask(__name__)

# Initialize the Sentiment Analysis Agent
sentiment_analyzer = pipeline("sentiment-analysis")


@app.route("/")
def home():
    return render_template("index.html")  # We will create this file later

@app.route("/query", methods=["POST"])
def handle_query():
    user_input = request.json.get("query", "").strip()

    # Basic validation
    if not user_input:
        return jsonify({"error": "Query cannot be empty."}), 400
    if len(user_input) > 512:
        return jsonify({"error": "Query is too long. Please limit to 512 characters."}), 400

    # Clean the query
    cleaned_query = clean_query(user_input)

    # Perform sentiment analysis
    sentiment_result = sentiment_analyzer(cleaned_query)[0]

    # Return the cleaned query and sentiment analysis result
    response = {
        "cleaned_query": cleaned_query,
        "sentiment": sentiment_result["label"],
        "confidence": sentiment_result["score"]
    }
    return jsonify(response)




if __name__ == "__main__":
    app.run(debug=True)
