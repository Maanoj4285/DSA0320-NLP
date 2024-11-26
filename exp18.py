import re

class FOPCParser:
    def __init__(self, expression):
        self.expression = expression.strip()

    def parse(self):
        return re.findall(r"[A-Za-z]+\([A-Za-z,]+\)|[∧∨¬→↔()]", self.expression)

# Example usage
expression = "\u2227Human(Socrates) ∨ Mortal(Socrates) → Mortal(x)"
parser = FOPCParser(expression)
parsed_tokens = parser.parse()
print("Parsed Tokens:", parsed_tokens)


print("\u2228 \u00AC \u2192 \u2194")
