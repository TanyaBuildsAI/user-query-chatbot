"""
Response Assembly Agent
Combines outputs from multiple agents into a coherent, user-friendly response.
"""
# Response Assembly Agent
"""
Combines outputs from multiple agents into a coherent, user-friendly response.
"""

from rag_agent import query_rag
from sentiment_analysis import analyze_sentiment

result = analyze_sentiment("This is a great product!")
print(result)

def assemble_response(user_query, product_info, sentiment_result):
    """
    Assemble the chatbot's response based on sentiment and product information.
    """
    # Determine tone based on sentiment
    if sentiment_result["label"] == "NEGATIVE":
        tone = "I'm here to help with your concern."
    elif sentiment_result["label"] == "POSITIVE":
        tone = "Great choice! Here's what I found for you:"
    else:
        tone = "Here's what I found for you:"
    
    # Combine tone with product details
    response = f"{tone}\n\n" \
               f"Product: {product_info['name_title']}\n" \
               f"Description: {product_info['description']}\n" \
               f"Price: {product_info['sale_price']}\n" \
               f"Rating: {product_info['average_product_rating']}"
    return response


    # Include product details from RAG output
    if rag_output:
        response += f"Product: {rag_output.get('name_title', 'N/A')}\n"
        response += f"Description: {rag_output.get('description', 'N/A')}\n"
        response += f"Price: {rag_output.get('sale_price', 'N/A')}\n"
        response += f"Rating: {rag_output.get('average_product_rating', 'N/A')}\n\n"
    else:
        response += "No relevant products found.\n\n"

    # Include sentiment analysis if provided
    if sentiment:
        response += f"Sentiment Analysis: {sentiment.get('label', 'N/A')} (Confidence: {sentiment.get('score', 'N/A')})\n"

    return response

def assemble_final_response(user_query):
    """
    Combines outputs from all agents and assembles the final response.

    Parameters:
    - user_query (str): The user's query.

    Returns:
    - str: A cohesive, user-friendly response.
    """
    try:
        # RAG agent retrieves relevant data
        rag_output = query_rag(user_query)
        if not rag_output:
            rag_output = {"name_title": "No matching product", "description": "N/A", "sale_price": "N/A", "average_product_rating": "N/A"}

        # Sentiment Analysis agent processes the query sentiment
        sentiment_output = analyze_sentiment(user_query)

        # Use the Response Assembly Agent to format the response
        response = assemble_response(user_query, rag_output, sentiment_output)
    except Exception as e:
        response = f"An error occurred while processing your query: {str(e)}"

    return response

# Test the function
if __name__ == "__main__":
    user_query = "Find me a budget-friendly smartphone."
    final_response = assemble_final_response(user_query)
    print(final_response)
