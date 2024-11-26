import nltk
from nltk import RegexpTagger

# Define regex-based rules for tagging
patterns = [
    (r'.*ing$', 'VERB'),       # Words ending with 'ing' are likely verbs
    (r'.*ed$', 'VERB'),        # Words ending with 'ed' are likely past-tense verbs
    (r'.*es$', 'VERB'),        # Words ending with 'es' are likely verbs
    (r'.*ly$', 'ADV'),         # Words ending with 'ly' are likely adverbs
    (r'.*ion$', 'NOUN'),       # Words ending with 'ion' are likely nouns
    (r'.*ment$', 'NOUN'),      # Words ending with 'ment' are likely nouns
    (r'[Tt]he', 'DET'),        # Specific rule for 'the' or 'The'
    (r'[Aa]nd', 'CONJ'),       # Specific rule for 'and' or 'And'
    (r'.*', 'NOUN')            # Default rule: anything else is a noun
]

# Create the RegexpTagger with the defined patterns
tagger = RegexpTagger(patterns)

# Test sentence
sentence = "The quick brown fox jumps over the lazy dog beautifully."

# Tokenize the sentence
words = nltk.word_tokenize(sentence)

# Tag the words using the rule-based tagger
tagged_sentence = tagger.tag(words)

# Display the tagged sentence
print("Tagged Sentence:", tagged_sentence)
