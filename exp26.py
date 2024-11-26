from transformers import MarianMTModel, MarianTokenizer

# Load the pre-trained MarianMT model and tokenizer for English to French translation
model_name = 'Helsinki-NLP/opus-mt-en-fr'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Function to translate text
def translate_text(text, model, tokenizer):
    # Tokenize the input text
    tokens = tokenizer.encode(text, return_tensors="pt")
    
    # Perform the translation
    translated_tokens = model.generate(tokens, max_length=256, num_beams=4, early_stopping=True)
    
    # Decode the translated tokens to text
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    
    return translated_text

# Example English text
english_text = "hello manoj"

# Translate English to French
french_translation = translate_text(english_text, model, tokenizer)
print(f"English: {english_text}")
print(f"French: {french_translation}")
