# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Use the .sort() method:
# Use a helper function to return the "num" key of each dictionary for comparison.
# Sort the list from greatest to least by the count.
# Import and call the function in main.py, and capture the result.
# Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it. (Be sure to match the expected output in the CLI tests!)
def sort_key(e):
    return e["num"]


def sort_dict(dict):
    list_of_dicts = []
    for entry in dict:
        pretty_dict = {}
        pretty_dict["char"] = entry
        pretty_dict["num"] = dict[entry]
        list_of_dicts.append(pretty_dict)

    return list_of_dicts


def get_character_counts(text):
    char_count = {}
    for word in text:
        for char in word:
            try:
                char_count[char.lower()] += 1
            except KeyError:
                char_count[char.lower()] = 1

    return char_count


def count_text_words(text):
    num = text.split()
    count = len(num)
    # print(num)
    return f"Found {count} total words\n"
