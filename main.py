def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    from stats import count_words, count_characters, sorted_list
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    report = sorted_list(num_characters)
    print( f"============ BOOKBOT ============\n"
         f"Analyzing book found at {book_path}...\n"
         f"----------- Word Count -----------\n"
         f"Found {num_words} total words\n"
         f"----------- Character Count -----------\n")
    for char in report:
        print(f"{char['char']}: {char['num']}")
    print(f"============= END ===============")




main()


