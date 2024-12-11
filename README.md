# User Query Chatbot

## Overview
The **User Query Chatbot** is an interactive tool designed to process user queries, analyze sentiment, and provide real-time feedback. It serves as a modular agent that integrates with other components, such as the **Sentiment Analysis Agent**, and can be extended with additional features like retrieval-augmented generation (RAG).

## Features
- **Query Cleaning and Validation**: Ensures user input is sanitized and meets length requirements.
- **Sentiment Analysis**: Analyzes user input for sentiment (Positive/Negative) using Hugging Face transformers.
- **Interactive Web Interface**: A responsive and styled chatbot interface for real-time user interaction.

## Folder Structure
user_query_agent/ ├── app.py # Main Flask application ├── query_processing.py # Helper functions for query cleaning ├── templates/ │ └── index.html # Frontend HTML template ├── static/ │ └── style.css # CSS for styling the chatbot interface ├── README.md # Documentation


## How to Run
1. Clone the repository:
   ```bash
   git clone git@github.com:TanyaBuildsAI/user-query-chatbot.git
   cd user-query-chatbot

2. Create a virtual environment and install dependencies:
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install flask transformers

3.Start the Flask app:
bash
Copy code
python app.py
Open your browser and go to: http://127.0.0.1:5000
