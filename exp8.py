import nltk
from collections import Counter, defaultdict
from nltk.tokenize import word_tokenize

# Download required datasets
nltk.download('brown')
nltk.download('universal_tagset')
nltk.download('punkt')

# Load tagged words from the Brown corpus
corpus = nltk.corpus.brown.tagged_words(tagset='universal')

# Train the model
def train_pos_tagger(corpus):
    word_tag_counts = defaultdict(Counter)  # Counts of (word, tag)
    tag_counts = Counter()                  # Counts of tags

    for word, tag in corpus:
        word_tag_counts[word.lower()][tag] += 1
        tag_counts[tag] += 1

    # Calculate probabilities
    word_tag_probs = {}
    for word, tag_count in word_tag_counts.items():
        word_tag_probs[word] = {tag: count / tag_counts[tag] for tag, count in tag_count.items()}
    
    return word_tag_probs
 
# Tagging function
def simple_pos_tagger(sentence, word_tag_probs):
    words = word_tokenize(sentence.lower())
    tagged_sentence = []

    for word in words:
        tag_probs = word_tag_probs.get(word, {"NOUN": 1})  # Default to NOUN if word is unseen
        best_tag = max(tag_probs, key=tag_probs.get)  # Pick the tag with the highest probability
        tagged_sentence.append((word, best_tag))
    
    return tagged_sentence

# Train the model
word_tag_probs = train_pos_tagger(corpus)

# Test the tagger
test_sentence = "The quick brown fox jumps over the lazy dog."
tagged_sentence = simple_pos_tagger(test_sentence, word_tag_probs)
print("Tagged Sentence:", tagged_sentence)
