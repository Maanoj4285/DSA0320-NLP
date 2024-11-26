import nltk
from nltk import CFG, ChartParser
from nltk.tree import Tree

# Define the context-free grammar (CFG)
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'park'
    V -> 'chased' | 'saw'
    P -> 'in' | 'with'
""")

# Initialize the parser
parser = ChartParser(grammar)

# Input sentence
sentence = "the dog chased a cat".split()

# Generate the parse trees
print("Parsing the sentence:")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()  # Display the parse tree in a readable format

    # Optionally, draw the parse tree (requires a GUI environment)
    # tree.draw()
