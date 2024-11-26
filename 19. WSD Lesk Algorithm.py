

import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import defaultdict


def lesk(context_sentence, ambiguous_word):
    max_overlaps = 0
    best_sense = None
    context = set(word_tokenize(context_sentence))

    for sense in wordnet.synsets(ambiguous_word):
        signature = set(word_tokenize(sense.definition()))
        for example in sense.examples():
            signature.update(word_tokenize(example))
        overlaps = len(context.intersection(signature))

        if overlaps > max_overlaps:
            max_overlaps = overlaps
            best_sense = sense

    return best_sense

# Example usage
sentence = "I went to the bank to deposit money"
ambiguous_word = "bank"
sense = lesk(sentence, ambiguous_word)

print(f"Context Sentence: {sentence}")
print(f"Ambiguous Word: {ambiguous_word}")
print(f"Best Sense: {sense}")
print(f"Definition: {sense.definition()}")
