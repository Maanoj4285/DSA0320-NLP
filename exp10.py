import re

# Sample text
text = "The quick brown fox jumps over the lazy dog"

# Tokenize the text into words
tokens = text.split()

# Initial tagging: Tag all words as nouns (NN)
initial_tags = [(word, 'NN') for word in tokens]


# Define transformation rules
# Each rule is a tuple (condition, current_tag, new_tag)
rules = [
    (lambda word, tag: re.fullmatch(r'[Tt]he', word), 'NN', 'DET'),
    (lambda word, tag: re.fullmatch(r'[Qq]uick|[Bb]rown|[Ll]azy', word), 'NN', 'JJ'),
    (lambda word, tag: re.fullmatch(r'fox|dog', word), 'NN', 'NN'),
    (lambda word, tag: re.fullmatch(r'jumps', word), 'NN', 'VBZ'),
    (lambda word, tag: re.fullmatch(r'over', word), 'NN', 'IN')
]

# Function to apply rules
def apply_rules(tokens, tags, rules):
    for i, (word, tag) in enumerate(tags):
        for rule in rules:
            condition, current_tag, new_tag = rule
            if condition(word, tag) and tag == current_tag:
                tags[i] = (word, new_tag)
    return tags

print(initial_tags)
# Apply the transformation rules to the initial tags
transformed_tags = apply_rules(tokens, initial_tags, rules)

# Display the results
print("Initial Tags: ", initial_tags)
print("Transformed Tags: ", transformed_tags)
