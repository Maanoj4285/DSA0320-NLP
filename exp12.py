class EarleyParser:
    def __init__(self, grammar, start_symbol):
        """
        Initialize the Earley parser with a grammar and start symbol.
        :param grammar: Dictionary where keys are non-terminals, and values are lists of productions.
        :param start_symbol: The start symbol of the grammar.
        """
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, input_tokens):
        """
        Parse the input tokens using the Earley algorithm.
        :param input_tokens: A list of input tokens.
        :return: True if the input matches the grammar, False otherwise.
        """
        n = len(input_tokens) + 1
        chart = [[] for _ in range(n)]

        # Add initial state
        chart[0].append((self.start_symbol, [], [self.start_symbol], 0))  # S → · StartSymbol, from position 0

        for i in range(n):
            for state in chart[i]:
                lhs, matched, remaining, origin = state

                if not remaining:  # Completion
                    self._complete(chart, state, i)
                elif remaining[0] in self.grammar:  # Prediction
                    self._predict(chart, remaining[0], i)
                elif i < len(input_tokens) and remaining[0] == input_tokens[i]:  # Scanning
                    self._scan(chart, state, i, input_tokens)

        # Check if the start symbol is fully parsed
        final_state = (self.start_symbol, [self.start_symbol], [], 0)
        return final_state in chart[-1]

    def _predict(self, chart, non_terminal, position):
        """
        Add predictions for the non-terminal to the chart.
        """
        for production in self.grammar[non_terminal]:
            state = (non_terminal, [], production, position)
            if state not in chart[position]:
                chart[position].append(state)

    def _scan(self, chart, state, position, input_tokens):
        """
        Match a terminal and add the new state to the chart.
        """
        lhs, matched, remaining, origin = state
        if position < len(input_tokens) and remaining[0] == input_tokens[position]:
            new_state = (lhs, matched + [remaining[0]], remaining[1:], origin)
            chart[position + 1].append(new_state)

    def _complete(self, chart, state, position):
        """
        Complete a rule and add results to parent states in the origin chart.
        """
        lhs, matched, remaining, origin = state
        for parent_state in chart[origin]:
            plhs, pmatched, premaining, porigin = parent_state
            if premaining and premaining[0] == lhs:
                new_state = (plhs, pmatched + [lhs], premaining[1:], porigin)
                if new_state not in chart[position]:
                    chart[position].append(new_state)


# Example Grammar
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["dog"], ["cat"]],
    "V": [["chased"], ["saw"]]
}

# Initialize parser
parser = EarleyParser(grammar, "S")

# Input string
input_string = "the dog chased a cat".split()

# Parse the input
result = parser.parse(input_string)

# Output result
if result:
    print(f"The string '{' '.join(input_string)}' is valid according to the grammar.")
else:
    print(f"The string '{' '.join(input_string)}' is NOT valid according to the grammar.")
