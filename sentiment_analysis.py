import sys
from transformers import pipeline

# Specify the model explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

def analyze_sentiment(text):
    """
    Perform sentiment analysis on the input text.
    """
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
    result = sentiment_analyzer(text)[0]

    # Set a threshold for confidence
    threshold = 0.75
    if result["score"] < threshold:
        result["label"] = "NEUTRAL"

    return result

def main():
    """
    Main function to process input and output files for sentiment analysis.
    """
    if len(sys.argv) < 3:
        print("Usage: python sentiment_analysis.py <input_file> <output_file>")
        sys.exit(1)

    # File paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Batch size (number of inputs to process at a time)
    batch_size = 10

    try:
        # Read input sentences from the file
        with open(input_file, "r") as file:
            texts = [line.strip() for line in file.readlines() if line.strip()]  # Remove blank lines

        if not texts:
            print("Error: Input file is empty or contains only blank lines.")
            sys.exit(1)

        # Divide inputs into batches
        batches = [texts[i:i + batch_size] for i in range(0, len(texts), batch_size)]

        # Process each batch and write results to the output file
        with open(output_file, "w") as file:
            for batch in batches:
                results = sentiment_analyzer(batch)
                for text, result in zip(batch, results):
                    file.write(f"Text: {text}\n")
                    file.write(f"Sentiment: {result['label']}, Confidence: {result['score']:.2f}\n\n")

        print(f"Sentiment analysis completed. Results saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred during sentiment analysis: {e}")

# Allow the script to be run standalone or imported as a module
if __name__ == "__main__":
    main()
