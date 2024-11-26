def transition(word):
    if word.endswith('y') and not word.endswith(('ay', 'ey', 'iy', 'oy', 'uy')):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh','o')):
        return word + 'es'
    elif word.endswith('f'):
        return word[:-1] + 'ves'
    elif word.endswith('fe'):
        return word[:-2] + 'ves'
    else:
        return word + 's'


# Test cases
nouns = ["cat", "dog", "bus", "box", "baby", "leaf", "tomato","toy"]
plural_nouns = {noun: transition(noun) for noun in nouns}

print("Plural Forms:")
for noun, plural in plural_nouns.items():
    print(f"{noun} -> {plural}")
