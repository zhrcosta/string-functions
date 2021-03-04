

def charCounter(string):

    # This function shows the number of each letter in a string.

    char_rank = []

    for decimal in range(255):  # range of ASCII lower case letter

        value = string.count(chr(decimal))
        if value > 0:
            char_rank.append((value, chr(decimal)))

    char_rank = sorted(char_rank)[::-1]

    for char in char_rank:
        print(f'| {char[1]} | ...... {char[0]}')


if __name__ == '__main__':
    
    s = 'This function shows the number of each letter in a string.'

    charCounter(s)
