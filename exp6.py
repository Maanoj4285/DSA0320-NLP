"""import random
from collections import defaultdict, Counter

def build_bigram_model(text):
    # Tokenize text into words
    words = text.split()
    
    # Create bigrams
    bigrams = [(words[i], words[i+1]) for i in range(len(words) - 1)]
    
    # Count occurrences of bigrams and individual words
    bigram_counts = Counter(bigrams)
    print(bigram_counts)
    word_counts = Counter(words)
    print(word_counts)
    # Calculate conditional probabilities for the bigrams
    bigram_model = defaultdict(dict)
    for (w1, w2), count in bigram_counts.items():
        bigram_model[w1][w2] = count / word_counts[w1]
    
    return bigram_model

def generate_text(bigram_model, start_word, length=10):
    # Generate text starting from the given word
    current_word = start_word
    result = [current_word]
    
    for _ in range(length - 1):
        next_word_candidates = bigram_model.get(current_word, {})
        if not next_word_candidates:
            break  # No valid next word, stop generation
        
        # Choose the next word based on probabilities
        next_word = random.choices(
            list(next_word_candidates.keys()), 
            weights=list(next_word_candidates.values())
        )[0]
        result.append(next_word)
        current_word = next_word
    
    return ' '.join(result)

# Sample text
sample_text = """"""
The quick brown fox jumps over the lazy dog. 
The dog barked back at the fox. The fox ran away quickly.
""""""

# Build bigram model
bigram_model = build_bigram_model(sample_text)

# Generate text
start_word = "The"
generated_text = generate_text(bigram_model, start_word, length=15)
print("Generated Text:", generated_text)"""
import random
from collections import defaultdict
text = """The quick brown fox jumps over the lazy dog. 
The dog barked back at the fox. The fox ran away quickly."""
tokens = text.split()
bigrams = defaultdict(list)
for i in range(len(tokens) - 1):
    bigrams[tokens[i]].append(tokens[i + 1])
current_word = random.choice(tokens)
generated_text = [current_word]
for _ in range(10):
    if current_word in bigrams:
        next_word = random.choice(bigrams[current_word])
        generated_text.append(next_word)
        current_word = next_word
    else:
        break
print("Generated Text:", " ".join(generated_text))

