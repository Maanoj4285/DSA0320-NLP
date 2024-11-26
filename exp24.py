import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK data is downloaded
#nltk.download('punkt')

# Define training data: Adding 'exclamatory' as a dialog act
training_data = [
    ("Can you help me?", "question"),
    ("What is the time now?", "question"),
    ("I need assistance with my account.", "request"),
    ("Please open the door.", "request"),
    ("This is a great opportunity!", "statement"),
    ("The weather is nice today.", "statement"),
    ("Could you explain this to me?", "question"),
    ("I would like some coffee.", "request"),
    ("It is raining outside.", "statement"),
    ("Wow, that's amazing!", "exclamatory"),
    ("Oh no, I forgot my keys!", "exclamatory"),
    ("Yay, we won the game!", "exclamatory"),
    ("What a beautiful sunset!", "exclamatory"),
]

# Feature extraction function
def extract_features(sentence):
    words = word_tokenize(sentence.lower())
    return {word: True for word in words}

# Prepare training data for Naive Bayes Classifier
labeled_features = [(extract_features(text), label) for text, label in training_data]

# Train the Naive Bayes Classifier
classifier = NaiveBayesClassifier.train(labeled_features)

# Function to predict dialog acts
def predict_dialog_act(utterance):
    features = extract_features(utterance)
    return classifier.classify(features)

# Sample conversation with exclamatory utterances
conversation = [
    "Can you tell me where the library is?",
    "Wow, that's incredible!",
    "The library is down the hall.",
    "Oh no, I forgot my wallet!",
    "What time does it open?",
    "Yay, I got an A on my test!",
]

# Recognize dialog acts in the conversation
print("Dialog Act Recognition:")
for utterance in conversation:
    act = predict_dialog_act(utterance)
    print(f"Utterance: {utterance}\nDialog Act: {act}\n")
