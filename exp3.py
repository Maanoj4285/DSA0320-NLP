import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text = "The children are playing with their toys and running outside."

words = word_tokenize(text)
print(f"Tokenized Words: {words}")

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(f"Lemmatized Words: {lemmatized_words}")

lemmatized_words_pos = [lemmatizer.lemmatize(word, pos='v') for word in words]
print(f"Lemmatized Words with POS: {lemmatized_words_pos}")
