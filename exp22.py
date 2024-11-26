import spacy
import coreferee

# Load the SpaCy language model with coreferee
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('coreferee')

def resolve_references(text):

    # Process the text using SpaCy
    doc = nlp(text)
    
    # Placeholder for resolved text
    resolved_text = text

    # Perform coreference resolution
    for cluster in doc._.coref_chains:
        # Iterate over each coreference chain
        for coref in cluster:
            # Replace pronouns with the most representative mention
            if len(coref) > 1:
                representative = coref[0]._.text  # Use the first mention as the representative
                for mention in coref[1:]:  # Replace subsequent mentions
                    resolved_text = resolved_text.replace(mention.text, representative)
    
    return resolved_text

if __name__ == "__main__":
    # Input text
    text = """
    John went to the park. He saw a dog there. It was barking loudly. 
    Mary was annoyed because it disturbed her reading.
    """
    
    # Resolve references
    resolved_text = resolve_references(text)
    
    print("Original Text:")
    print(text)
    print("\nText with Resolved References:")
    print(resolved_text)
