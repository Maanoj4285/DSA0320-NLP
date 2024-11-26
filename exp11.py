class TopDownParser:
    def __init__(self, grammar, start_symbol):
        """
        Initialize the parser with a grammar and start symbol.
        :param grammar: Dictionary where keys are non-terminals, and values are lists of possible productions.
        :param start_symbol: The start symbol of the grammar.
        """
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, tokens):
        """
        Start the parsing process for the given tokens.
        :param tokens: List of input tokens.
        :return: True if the string is valid according to the grammar, otherwise False.
        """
        return self._match(self.start_symbol, tokens)

    def _match(self, non_terminal, tokens):
        """
        Attempt to match a non-terminal with the input tokens.
        :param non_terminal: Current non-terminal being expanded.
        :param tokens: Remaining input tokens.
        :return: True if the string matches, otherwise False.
        """
        if non_terminal not in self.grammar:
            # If the non-terminal is not in the grammar, treat it as a terminal
            return tokens and tokens[0] == non_terminal, tokens[1:] if tokens else tokens

        # Try each production rule for the non-terminal
        for production in self.grammar[non_terminal]:
            remaining_tokens = tokens[:]
            success = True

            # Try matching each symbol in the production
            for symbol in production:
                if isinstance(symbol, str):
                    result, remaining_tokens = self._match(symbol, remaining_tokens)
                    if not result:
                        success = False
                        break
                else:
                    success = False

            # If the production matches, return True
            if success:
                return True, remaining_tokens

        return False, tokens


# Define a grammar (context-free grammar)
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["dog"], ["cat"]],
    "V": [["chased"], ["saw"]]
}

# Initialize parser
parser = TopDownParser(grammar, "S")

# Example input strings
input_string = "the dog chased a dog".split()
result, remaining = parser.parse(input_string)

if result and not remaining:
    print(f"The string {' '.join(input_string)} is valid according to the grammar.")
else:
    print(f"The string {' '.join(input_string)} is NOT valid according to the grammar.")
