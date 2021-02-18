"""
    Função para inverter os caracteres de uma STRING método 2
"""


def reverseString(string):

    reversed = ""

    for character in list(string):
        reversed = character + reversed

    return reversed


print(reverseString("zhrcosta"))
