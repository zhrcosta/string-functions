

def reverseString(string):

    # Função para inverter os caracteres de uma STRING método 1

    reversed = ""

    for index in range(1, len(string)+1):
        reversed += string[-index]

    return reversed


print(reverseString("zhrcosta"))
