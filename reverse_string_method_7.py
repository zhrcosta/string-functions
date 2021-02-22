

def reverseString(string):

    # Função para inverter os caracteres de uma STRING método 7

    string = "".join([string[-index] for index in range(1, len(string)+1)])

    return string


print(reverseString("zhrcosta"))
