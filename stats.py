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

def sort_on(dict):
    return dict["num"]

def sorted_list(char_counts_dict):
    char_list = []
    for character, count in char_counts_dict.items():
        if character.isalpha():
            dict_list = {"char": character, "num": count}
            char_list.append(dict_list)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    

