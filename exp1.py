import re

# Sample text
text = "The quick brown fox jumps over the lazy dog. Call me at 123-456-7890."

# 1. Match a word at the start of the string
pattern_start = r"^The"
match_start = re.match(pattern_start, text)
if match_start:
    print(f"Matched at the start: {match_start.group()}")

# 2. Search for a phone number pattern
pattern_phone = r"\d{3}-\d{3}-\d{4}"
search_phone = re.search(pattern_phone, text)
if search_phone:
    print(f"Phone number found: {search_phone.group()}")

# 3. Find all words that start with a vowel
pattern_vowels = r"\b[aeiouAEIOU]\w*"
find_vowels = re.findall(pattern_vowels, text)
print(f"Words starting with a vowel: {find_vowels}")

# 4. Replace all digits with an asterisk
pattern_digits = r"\d"
replaced_text = re.sub(pattern_digits, "*", text)
print(f"Text after replacing digits: {replaced_text}")

# 5. Split the text at spaces
pattern_spaces = r"\s+"
split_text = re.split(pattern_spaces, text)
print(f"Split text: {split_text}")
