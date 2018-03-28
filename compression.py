from collections import Counter

def compress_string(expanded_string):
    """Given a string with multiple characters compress it using the counts.
    Example:
    input = "aabccccaaa"
    output = "a2b1c4a3"
    """
    #Corner cases
    if expanded_string is None:
        return None
    if not expanded_string:
        return ""
    #I check if a letter i is the same as i+1, increasing the count if it's so
    compressed_string = []
    count = 0
    group = expanded_string[0]

    for letter in expanded_string:

        if letter != group:
            compressed_string.append(group + str(count))
            group = letter
            count = 0

        count +=1
    #don't forget about the last letter
    compressed_string.append(group + str(count))
    if len(compressed_string) >= len(expanded_string):
        return expanded_string
    return "".join(compressed_string)


def stringeator(func):
    """decorator thats return a function as a string"""

    def wrapper(word):
        return "".join(func(word))

    return wrapper


@stringeator
def compress(word):
    """same problem as before but using generators"""
    current_letter = word[0]
    count = 1
    for letter in word[1:]:
        if letter == current_letter:
            count += 1
        else:
            yield current_letter + str(count)
            current_letter = letter
            count = 1
    yield current_letter + str(count)
