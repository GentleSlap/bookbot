def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    from stats import count_words, count_characters
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(num_characters)

main()


