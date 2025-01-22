def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    lowered_string = text.lower()
    char_count = {}
    for character in lowered_string:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    list_char = list(char_count.items())
    return list_char

def sort_on(dict):
    return dict[1]

def main():
    with open("books/frankenstein.txt") as file:
        text = file.read()

        word_count = count_words(text)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        characters = count_character(text)
        characters.sort(reverse=True, key=sort_on)
       
        for key, value in characters:
            if key.isalpha():
                print(f"The '{key}' character was found {value} times")
        print(f"--- End report ---")

if __name__ == "__main__":
    main()