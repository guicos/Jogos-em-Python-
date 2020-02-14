import random
import adivinhacao

def dica(num):
    number = random.randrange(1,5)

    stop = (num % 2) == 0

    if( stop == True and number == 1):
        print("Numero é par")

    if( stop == False and number == 2 ):
        print("O numero é impar")

    if( number == 3):
        print(f"O numero esta abaixo de {num + 1 }")

    if (number == 4):
        print(f"O numero esta acima de {num - 2}")

    if (number == 5):
        print(f"Sortudo o numero é {num}")