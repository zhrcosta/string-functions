

def reverseString(string):

    # Função para inverter os caracteres de uma STRING método 3

    reversed = list(string)

    for index in range(len(reversed)):
        reversed.insert(index, reversed[-1])
        reversed.pop()

    reversed = "".join(reversed)

    return reversed


print(reverseString("zhrcosta"))
