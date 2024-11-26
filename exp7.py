    import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Ensure NLTK data is downloaded (run this once)
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(words)

# Print the result
print("POS Tags:", pos_tags)
