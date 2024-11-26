import spacy

def evaluate_coherence(text):
    """
    Evaluates the coherence of a given text by calculating the average similarity
    between consecutive sentences.

    Args:
        text (str): Input text to evaluate.

    Returns:
        float: Average coherence score (0 to 1).
    """
    # Load the spaCy language model
    nlp = spacy.load("en_core_web_md")

    # Process the text
    doc = nlp(text)

    # Extract sentences
    sentences = list(doc.sents)

    if len(sentences) < 2:
        print("The text must contain at least two sentences for coherence evaluation.")
        return 0.0

    # Calculate pairwise similarity between consecutive sentences
    similarities = []
    for i in range(len(sentences) - 1):
        similarity = sentences[i].similarity(sentences[i + 1])
        similarities.append(similarity)

    # Calculate the average coherence score
    average_coherence = sum(similarities) / len(similarities)
    return average_coherence


# Example usage
if __name__ == "__main__":
    sample_text = (
        "The sun was setting over the horizon, painting the sky in hues of orange and pink. "
        "Birds chirped softly as they settled into their nests. "
        "The gentle breeze carried the scent of blooming flowers."
    )
    coherence_score = evaluate_coherence(sample_text)
    print(f"Coherence Score: {coherence_score:.2f}")
