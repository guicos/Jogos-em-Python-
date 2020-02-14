def jogar():
    print(" _______")
    print("|(o)_(o)|")
    print("|_______|")
    print("   _|_")
    print("    |")
    print("    |")
    print("   / \ ")

    import random

    dados = 5
    with open('palavras.txt','w') as arquivo:
        print("Escolha 5 palavras para iniciar o jogo!")
        while dados > 0:
            lista = input("")
            arquivo.write(lista + '\n')
            dados -= 1
            print(f"Falta {dados} palavras")


    with open('palavras.txt','r') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()


    letras_acertadas = ["_" for letra in palavra_secreta]


    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = str(input("Qual letra: "))
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if( chute == letra ):
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print("Fim!")




if( __name__ == "__main__"):
    jogar()