def words_count(text):
    words = text.split()
    return len(words)

def characters_count(text):
    #define an empty dict:
    book_dict = {}
    #store all characters as lower cases:
    book_characters = text.low()


    

def sort_on(dict):
    pass

def main():
    try:
        with open("books/frankenstein.txt",encoding="utf-8") as file:
            stored_file = file.read()
            print(f"Raport date din 'frankenstein.txt'")
            print(f"Incepere raport #################")
            words = words_count(stored_file)
            print(f"Number of words: {words}")
            print(f"Finalizare raport ###############")
            ceva = "1 Doru Tudurachi".partition(" ")
            print(f"rezultat: {ceva}")

    except FileNotFoundError:
        print("Error: The file 'frankenstein.txt' was not found. Please check the file path.")
    except PermissionError:
        print("Error: You do not have permission to read the file. Please check your file permissions.")
    except OSError as e:
        print(f"An OS error occurred while trying to read the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    

if __name__ == "__main__":
    main()