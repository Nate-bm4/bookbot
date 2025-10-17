from stats import count_text_words, get_character_counts, sort_dict, sort_key
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = sys.argv
    # Check if user provided a file path

    try:
        if filepath[1]:
            pass
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============\n")
    book = get_book_text(filepath[1])

    print(f"Analyzing book found at {filepath[1]}\n")

    print("----------- Word Count ----------\n")
    # Calculate the amount of words in the book
    print(count_text_words(book))
    char_counts = get_character_counts(book)

    # sort the dictionary
    sorted_dict = sort_dict(char_counts)
    sorted_dict.sort(reverse=True, key=sort_key)
    print(""" --------- Character Count -------\n""")

    # Displaying character counts
    for dict in sorted_dict:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")


main()
