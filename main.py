import sys
from stats import num_of_words, num_of_characters, sorting, myFunc

def gwt_book_text(filename):
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = gwt_book_text(sys.argv[1])

    amount_of_words = num_of_words(book)
    amount_of_characters = num_of_characters(book)
    all_characters = sorting(book)
    all_characters.sort(reverse=True, key=myFunc)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {amount_of_words} total words")
    print("--------- Character Count -------")
    for character in all_characters:
        if character["char"] == " ":  # skip spaces
            continue
        print(f"{character["char"]}: {character['num']}")
    print("============= END ===============")