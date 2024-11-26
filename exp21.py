import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def get_meaning(noun_phrase):
    meanings = []
    for word in noun_phrase:
        synsets = wn.synsets(word, pos=wn.NOUN)
        if synsets:
            meanings.append(synsets[0].definition())
    return meanings

def extract_noun_phrases(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    # Define a chunk grammar to identify noun phrases
    grammar = "NP: {<DT>?<JJ>*<NN>+}"
    chunk_parser = RegexpParser(grammar)
    tree = chunk_parser.parse(tagged_words)

    noun_phrases = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            noun_phrase = [word for word, tag in subtree.leaves()]
            noun_phrases.append(noun_phrase)
    return noun_phrases

def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    noun_phrases = extract_noun_phrases(sentence)
    print(f"Sentence: {sentence}")
    print("Noun Phrases and their Meanings:")

    for np in noun_phrases:
        meaning = get_meaning(np)
        np_str = " ".join(np)
        print(f"Noun Phrase: {np_str}")
        if meaning:
            print(f"Meanings: {meaning}")
        else:
            print("Meanings: No meaning found in WordNet")

if __name__ == "__main__":
    main()
