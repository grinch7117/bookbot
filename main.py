from stats import count_words, count_characters


def get_book_text(path):
    contents = ''
    with open(path) as f:
        contents = f.read()

    return contents

def main():
    book_content = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_content)
    character_count = count_characters(book_content)

    print(f"Found {word_count} total words")
    print(character_count)

main()