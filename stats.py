def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def count_characters(text):
    characters_lower_case = str.lower(text)
    characters_count = {}
    for c in characters_lower_case:
        if c in characters_count:
            characters_count[c] += 1
        else:
                characters_count[c] = 1
    return characters_count   
