def number_of_words(book):
    words = book.split()
    count = 0

    for word in words:
        count += 1

    return count

def count_characters(book):
    chars = {}
    for character in book:
        if character.lower() not in chars:
            chars[character.lower()] = 1
        else:
            chars[character.lower()] += 1
    
    return chars

def helper(items):
    return items["num"]

def sorted_count(char_dict):
    # Returns a sorted LIST of dictionaries

    sorted_list = []
    for character in char_dict:
        sorted_list.append({"char": character, "num": char_dict[character]})

    sorted_list.sort(reverse=True, key=helper)

    return sorted_list
