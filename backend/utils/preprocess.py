
# backend/utils/preprocess.py

import re
from bs4 import BeautifulSoup

def clean_text(text):
    """
    Cleans text by removing HTML tags, extra spaces, and special characters.
    """
    if not text:
        return ""
    
    # Remove HTML tags using BeautifulSoup or regex
    # Using simple regex for speed as users requested simple clean
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove special characters but keep basic punctuation
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = text.strip()
    
    return text

def simple_tokenize(text):
    """
    Simple whitespace tokenizer
    """
    return text.split()
