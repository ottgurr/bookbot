
def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def count_characters(text):
    character_count = {}

    for character in text.lower():
        if character not in character_count:
            character_count[character] = 1
        elif character in character_count:
            character_count[character] += 1

    return character_count

def sort_on(item):
    return item["num"]

def sort_list(num_characters):
    List = []
    for key in num_characters:
        num = num_characters[key]
        List.append({"char": key, "num": num})
    List.sort(reverse=True, key=sort_on)
    return List