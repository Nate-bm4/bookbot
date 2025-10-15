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
    return f"Found {count} total words"
