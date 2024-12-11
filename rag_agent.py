import os
print("Current working directory:", os.getcwd())

import pandas as pd
def query_rag(user_query):
    """
    Retrieve relevant product information based on the user query.
    """
    # Example: Use keyword matching or similarity scoring
    matching_products = data[data["description"].str.contains(user_query, case=False, na=False)]
    
    if not matching_products.empty:
        # Return the first matching product for simplicity
        product = matching_products.iloc[0]
        return {
            "name_title": product["name_title"],
            "description": product["description"],
            "sale_price": product["sale_price"],
            "average_product_rating": product["average_product_rating"]
        }
    else:
        return {
            "name_title": "No product found",
            "description": "Sorry, no matching product.",
            "sale_price": "-",
            "average_product_rating": "-"
        }

# Load the cleaned dataset
dataset_path = "refined_jcpenney_data.csv"
data = pd.read_csv(dataset_path)

# Display a preview of the dataset
print("Dataset loaded successfully!")
print(data.head())
