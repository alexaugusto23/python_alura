def jogar():

    print("\n##################################")
    print("Bem vindos ao jogo da Forca!")
    print("\n##################################")

    lista = []
    for item in palavra_secreta:
        lista.append("_")
    print(lista)
    

    enforcou = False
    acertou = False


    while (not enforcou and not acertou):
        chute = input("Qual a letra: ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a Letra |{}| na posição |{}|".format(letra, index))
            index + 1
        print("jogando...")

    print("\nO Jogo Terminou !!!")

if (__name__ == "__main__"):
    jogar()