import sys

from stats import count_words, count_characters, generate_character_report


def get_book_text(path):
    contents = ''
    with open(path) as f:
        contents = f.read()

    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_content = get_book_text(sys.argv[1])
    word_count = count_words(book_content)
    character_report = generate_character_report(count_characters(book_content))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in character_report:
        print(f'{entry["char"]}: {entry["num"]}')

main()