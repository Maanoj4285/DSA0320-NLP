import nltk
from nltk.stem import PorterStemmer

# Download necessary NLTK data (if not already installed)
nltk.download('punkt')

# Initialize the PorterStemmer
stemmer = PorterStemmer()

# List of words to be stemmed
words = ["running", "jumps", "happily", "cats", "studied", "flying", "better"]

# Perform stemming on the list of words
stemmed_words = [stemmer.stem(word) for word in words]

# Output the original and stemmed words
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
