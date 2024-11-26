import nltk
from nltk import Nonterminal, PCFG
from nltk.parse import ViterbiParser

# Define the probabilistic context-free grammar
pcfg = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det Adj N [0.4]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'dog' [0.4] | 'cat' [0.3] | 'park' [0.3]
    Adj -> 'big' [0.5] | 'small' [0.5]
    V -> 'chased' [0.6] | 'saw' [0.4]
""")

# Initialize the Viterbi parser
parser = ViterbiParser(pcfg)

# Input sentence
sentence = "the big dog chased a cat".split()

# Parse the sentence
print(f"Parsing sentence: {' '.join(sentence)}\n")
for tree in parser.parse(sentence):
    # Print the most probable parse tree
    print("Most Probable Parse Tree:")
    print(tree)
    tree.pretty_print()  # Display the parse tree in a readable format

    # Show the probability of the parse
    print(f"Probability of this parse: {tree.prob()}")
