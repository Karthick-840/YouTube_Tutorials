import pandas as pd
from datetime import timedelta
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
nltk.download("punkt")

def convert_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
# Define a function to extract keywords from text
def extract_keywords(text):
    # Use regular expressions to remove special characters, symbols, and numbers
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize the cleaned text
    words = word_tokenize(cleaned_text)

    # Create a list of English stopwords and additional common words to exclude
    custom_stopwords = set(stopwords.words("english") + ["for", "or", "and", "the", "is", "are", "it", "in", "on"])
    
    # Remove punctuation, stopwords and common words and also lowercase the words
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in custom_stopwords]
    
    return words
