from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample set of documents
documents = [
    "The sky is blue and beautiful.",
    "The sun in the sky is bright.",
        "The sun is bright and the sky is blue.",
    "We can see the shining sun, the blue sky and the beautiful landscape."
]

# Define the query
query = "blue sky"

# Initialize the TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer on the documents and transform them into a matrix of TF-IDF features
tfidf_matrix = vectorizer.fit_transform(documents)

# Transform the query to the same vector space as the documents
query_tfidf = vectorizer.transform([query])

# Compute the cosine similarity between the query and each document
cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix)

# Rank the documents based on similarity (higher cosine similarity means more relevant)
ranking = cosine_similarities[0].argsort()[::-1]

# Display the ranking
print("Query:", query)
print("\nRanking of Documents based on similarity:")
for i, rank in enumerate(ranking):
    print(f"Rank {i+1}: Document {rank+1} (Similarity: {cosine_similarities[0][rank]:.4f})")
    print(f"Document: {documents[rank]}\n")
