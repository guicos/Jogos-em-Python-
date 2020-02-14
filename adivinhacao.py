def jogar():
    print ("  ______ ")
    print ("_|______|_")
    print ('|(o) | (o)|')
    print ('|   |/    |')
    print ('|)\_____/(|')
    print ("|_________|")

    import random
    import dica
    nivel = 0

    while nivel <= 0 or nivel >= 4:
        nivel = int(input("Escolha seu nivel \n Facil (1) \n Médio (2) \n Dificil(3) \n Aguardando: "))
        if (nivel == 1):
            tentativas = 10
        elif (nivel == 2):
            tentativas = 5
        elif (nivel == 3):
            tentativas = 3
        elif not nivel <= 0 or nivel >= 4:
            print("Coloque um numero valido!")



    chute = int(input("Escolha um numero: "))

    numero = random.randrange(1, 101)
    valor_real = chute == numero


    for rodadas in range(1, 5):

        if(chute == 1001):
            dica.dica(numero)

        if not(chute < 100 or chute > 1 or chute == 1001):
            print("comando proibido")
            print(f"Você ainda tem {tentativas} tentativas!")
            chute = int(input("Chute novamente: "))
            valor_real = chute == 43
            tentativas -= 1
            continue

        if (tentativas == 0):
            print("Você falhou!")
            break

        elif (chute > numero):
            print(f"Você ainda tem {tentativas} tentativas!" )
            chute = int(input("Chute novamente: "))
            valor_real = chute == 43
            tentativas -= 1

        elif (chute < numero):
            print(f"Você ainda tem {tentativas} tentativas!")
            chute = int(input("Chute novamente:"))
            valor_real = chute == 43
            tentativas -= 1

        else:
            print("Acertou!")
            break

if(__name__ == "__main__"):
    jogar()


