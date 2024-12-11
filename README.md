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
