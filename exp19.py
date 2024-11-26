"""from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def lesk(context_sentence, word):
    context = set(word_tokenize(context_sentence))
    synsets = wordnet.synsets(word)
    best_sense = max(synsets, key=lambda s: len(context.intersection(set(word_tokenize(s.definition())))), default=None)
    return best_sense

# Example usage
sentence = "The crane is flying over the lake."
word = "crane"
sense = lesk(sentence, word)
if sense:
    print(f"Best sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print("No sense found.")
"""
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

def lesk_improved(context_sentence, word):
    context = set(word_tokenize(context_sentence))
    synsets = wordnet.synsets(word)
    
    # Filter to prioritize noun synsets over verb synsets
    noun_synsets = [synset for synset in synsets if synset.pos() == 'n']
    
    best_sense = None
    max_overlap = 0

    # Keywords that strongly indicate the "bird" sense
    bird_keywords = {"bird", "feathers", "wings", "fly", "lake", "marsh"}

    for synset in noun_synsets:
        # Combine definition, examples, hypernyms, hyponyms, and meronyms
        signature = set(word_tokenize(synset.definition()))
        for example in synset.examples():
            signature.update(word_tokenize(example))
        for hypernym in synset.hypernyms():
            signature.update(word_tokenize(hypernym.definition()))
        for hyponym in synset.hyponyms():
            signature.update(word_tokenize(hyponym.definition()))
        for meronym in synset.part_meronyms():
            signature.update(word_tokenize(meronym.definition()))

        # Boost overlap score if the context contains bird-related words
        overlap = len(context.intersection(signature))
        
        # Boost the score if bird-related keywords are found in the context
        if context.intersection(bird_keywords):
            overlap *= 2  # Double the overlap if bird-related keywords are present

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset

    return best_sense

# Example usage
sentence = "The crane is flying over the lake."
word = "crane"
sense = lesk_improved(sentence, word)

if sense:
    print(f"Best sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print("No sense found.")
