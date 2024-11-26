from nltk.corpus import wordnet

# Input word
word = "Train"

# Retrieve synsets
synsets = wordnet.synsets(word)
print(f"Synsets for '{word}':")
for syn in synsets:
    print(f"- {syn.name()}: {syn.definition()}")

# Explore meanings
if synsets:
    print("\nExamples of usage:")
    for example in synsets[0].examples():
        print(f"- {example}")

# Synonyms and antonyms
synonyms = []
antonyms = []
for syn in synsets:
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.extend([ant.name() for ant in lemma.antonyms()])

print(f"\nSynonyms: {set(synonyms)}")
print(f"Antonyms: {set(antonyms)}")
