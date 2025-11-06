from stats import count_words, get_letter_counter
import sys

USAGE_MESSAGE = "Usage: python3 main.py <path_to_book>"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print(USAGE_MESSAGE)
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        book_text = get_book_text(book_path)
    except:
        print("Error: File Not Found")
        sys.exit(1)

    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    letter_counter = get_letter_counter(book_text)
    letter_counter = list(letter_counter.items())
    letter_counter.sort(reverse=True, key = lambda x: x[1])

    for letter, count in letter_counter:
        if letter == "\n":
            letter = "\\n"

        print(f"{letter}: {count}")

main()