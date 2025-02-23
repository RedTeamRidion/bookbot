def word_count(text):
    string_count = text.split()
    return len(string_count)

def character_count(text):
    unique = {}
    count = 0
    lower_case = text.lower()
    for letters in lower_case:
        if letters not in unique:
            unique[letters] = 1
        else:
            unique[letters] += 1
    return unique
    