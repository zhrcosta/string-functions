
def splitM1(string):

    # Função para separar uma frase ou texto, usando o espaço como separador, retornando uma lista de palavras.

    # Todos os caracteres diferentes de " "(espaço) são armazenados temporariamente aqui.
    word = ""

    # Lista que será retornada com os grupos de caracteres.
    word_list = []

    for character in string:

        # Cada valor diferente de (espaço) é concatenado em WORD.
        if not character == " ":
            word += character

        # Ao detectar um espaço na condição acima o grupo de caracteres é adicionado a lista.
        # E a variavel WORD é limpa para formação de uma nova palavra.
        else:
            if word != "":
                word_list.append(word)
                word = ""

    # Ao final da execução do Loop For a variável WORD pode conter um grupo de caracteres que deve ser adicionado a lista.
    if word != "":
        word_list.append(word)
        word = ""

    return word_list


print(splitM1("   Where     there    is    matter,   there is geometry    "))
