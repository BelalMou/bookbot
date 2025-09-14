from itertools import count


def num_of_words(text):
    return len(text.split())

def num_of_characters(text):
    all_chars = {}
    for char in text.lower():
        if char in all_chars:
            all_chars[char] += 1
        else:
            all_chars[char] = 1
    return all_chars