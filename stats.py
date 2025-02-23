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
    

def character_report(unique):
    sorted_list = []
    for pair, count in unique.items():
        new_dict = {"char": pair, "num": count}
        sorted_list.append(new_dict)
    def sort_on(new_dict):
        return new_dict["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    
