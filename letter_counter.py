

def letterCounter(string):

    # This function shows the number of each letter in a string.
    # Upper and lower case letters in this function are the same.

    string = string.lower()
    char_rank = []

    # range of ASCII lower case letter
    asciiNumber = list(range(97, 123))

    for decimal in asciiNumber:

        value = string.count(chr(decimal))

        if value > 0:

            char_rank.append((value, chr(decimal)))

    char_rank = sorted(char_rank)[::-1]

    for letter in char_rank:
        print(f'{letter[1]} ...... {letter[0]}')


if __name__ == '__main__':
    s = 'This function shows the number of each letter in a string.'
    letterCounter(s)
