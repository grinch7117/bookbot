def count_words(book_text):
    words = book_text.split()

    return len(words)

def count_characters(book_text):
    character_map ={}
    for character in book_text:
        character = character.lower()
        if character in character_map:
            character_map[character] += 1
        else:
            character_map[character] = 1

    return character_map