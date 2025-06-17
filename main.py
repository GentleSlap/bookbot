def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    from stats import count_words
    number_words = count_words(book_text)
    print(f"{number_words} words found in the document")

main()


