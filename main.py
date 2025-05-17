from stats import word_count, count_characters


def get_book_test(path):
    with open(path) as f:
      return f.read()
        
def main():
    path="books/frankenstein.txt"
    book_text = get_book_test(path)
    num_words = word_count(book_text)
    char_distribution = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(char_distribution)

if __name__ == "__main__":
    main()

