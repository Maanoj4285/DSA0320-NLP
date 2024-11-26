import nltk
from nltk import CFG, ChartParser

# Define a context-free grammar with explicit agreement rules
grammar = CFG.fromstring("""
    S -> NP_sg VP_sg | NP_pl VP_pl
    NP_sg -> Det N_sg
    NP_pl -> Det N_pl
    VP_sg -> V_sg NP_sg | V_sg NP_pl
    VP_pl -> V_pl NP_sg | V_pl NP_pl
    Det -> 'the'
    N_sg -> 'dog' | 'cat'
    N_pl -> 'dogs' | 'cats'
    V_sg -> 'chases' | 'sees'
    V_pl -> 'chase' | 'see'
""")

# Initialize the parser
parser = ChartParser(grammar)

def check_agreement(sentence):
    """
    Check subject-verb agreement for a given sentence using CFG.
    :param sentence: A string sentence to check.
    :return: Valid or invalid agreement message.
    """
    tokens = sentence.split()
    valid = False

    print(f"\nChecking sentence: '{sentence}'")
    for tree in parser.parse(tokens):
        print("Parse Tree:")
        tree.pretty_print()  # Display the parse tree
        valid = True  # If the sentence parses, it follows the agreement rules
    
    if valid:
        return f"The sentence '{sentence}' is grammatically correct."
    else:
        return f"The sentence '{sentence}' has agreement errors."

# Example Sentences
sentences = [
    "the dog chases the cat",   # Correct
    "the dogs chase the cat",  # Correct
    "the cat chase the dog",   # Incorrect
    "the dogs chases the cats" # Incorrect
]

# Check each sentence
for sent in sentences:
    result = check_agreement(sent)
    print(result)
