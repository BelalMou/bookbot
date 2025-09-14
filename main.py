
from stats import num_of_words, num_of_characters

def gwt_book_text(filename):
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    book = gwt_book_text("books/frankenstein.txt")
    print(f"{num_of_words(book)} words found in the document")
    print(num_of_characters(book))