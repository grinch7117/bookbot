def get_book_text(path):
    contents = ''
    with open(path) as f:
        contents = f.read()

    return contents

def count_words(book_text):
    words = book_text.split()
    return len(words)

def main():
    book_content = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_content)

    print(f"Found {word_count} total words")

main()