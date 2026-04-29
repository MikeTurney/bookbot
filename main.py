from stats import number_of_words, count_characters, sorted_count
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    try:
        book_location = sys.argv[1]
        book = get_book_text(book_location)
        chars = count_characters(book)
        char_count = sorted_count(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words(book)} total words")
        print("--------- Character Count -------")
        for item in char_count:
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

main()
