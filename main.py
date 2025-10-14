from stats import count_text_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = (
        "/Users/ndowns/Code/workspace/github/projects/bookbot/books/frankenstein.txt"
    )
    book = get_book_text(filepath)
    print(count_text_words(book))


main()
