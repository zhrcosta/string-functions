

def reverseString(string):

    # Função para inverter os caracteres de uma STRING método 5

    string = list(string)[::-1]
    string = "".join(string)

    return string


print(reverseString("zhrcosta"))
