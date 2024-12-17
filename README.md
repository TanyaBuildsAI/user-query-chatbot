# E-Commerce Chatbot

This project is an AI-powered chatbot for e-commerce support, combining **Retrieval-Augmented Generation (RAG)** and **Sentiment Analysis** to provide dynamic, tone-aware product recommendations.

---

## Current Features

### Chatbot Capabilities
1. **Dynamic Responses:**
   - Fetches product information from a dataset based on user queries.
   - Provides responses tailored to user sentiment.

2. **Sentiment Analysis:**
   - Adjusts response tone based on detected sentiment (Positive, Neutral, Negative).

3. **RAG Integration:**
   - Searches an e-commerce dataset to find relevant product information.
   - Returns product details such as name, description, price, and rating.

### Example Interactions
#### Query: "Can you help me find a new pair of capris?"
**Response:**
I'm here to help with your concern.

Product: Example Product
Description: This is an example description.
Price: $99
Rating: 4.5

### Installation Instructions
Clone the Repository:
git clone https://github.com/YourUsername/Ecommerce-Chatbot.git
cd Ecommerce-Chatbot

### Set Up the Environment:
- python -m venv venv
- source venv/bin/activate  # For macOS/Linux
- venv\Scripts\activate     # For Windows
- pip install -r requirements.txt

### Run the Flask App:
flask run
Access the Chatbot: Open a browser and navigate to http://127.0.0.1:5000
