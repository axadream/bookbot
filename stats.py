def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_map = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in character_map:
            character_map[char] +=1
        else:
            character_map[char] = 1
    return character_map 

