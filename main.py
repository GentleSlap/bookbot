def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    number_words = count_words(book_text)
    print(f"{number_words} words found in the document")

main()


