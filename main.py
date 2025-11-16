def get_book_text(path):
    contents = ''
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)

main()