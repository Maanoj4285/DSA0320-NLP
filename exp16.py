import spacy

# Load the SpaCy language model
nlp = spacy.load("en_core_web_sm")  # Use 'en_core_web_md' or 'en_core_web_lg' for larger models

# Input text
text = """
Apple Inc. is planning to open a new office in London. Tim Cook announced the plans during a meeting with UK officials last Tuesday.
"""

# Process the text with SpaCy
doc = nlp(text)

# Print Named Entities
print("Named Entities, their labels, and positions:")
for ent in doc.ents:
    print(f"Text: {ent.text}, Label: {ent.label_}, Start: {ent.start_char}, End: {ent.end_char}")
