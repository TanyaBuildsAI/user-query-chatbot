import re

def clean_query(query):
    """
    Cleans and preprocesses the user query.
    - Removes extra spaces.
    - Strips special characters (except punctuation and letters).
    """
    # Remove unnecessary spaces
    query = query.strip()
    
    # Remove special characters except basic punctuation
    query = re.sub(r"[^a-zA-Z0-9 .,!?'-]", "", query)
    
    return query
