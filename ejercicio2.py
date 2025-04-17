import random

numero = random.randint(1, 10)

for i in range(3):
    intento = int(input("adivina el numero del 1 al 10: "))
    if intento == numero:
        print("adivinaste!, este es el nuemro")
        break
    elif intento < numero:
        print("muy bajo el numero.")
    else:
        print("muy alto numero.")

if intento != numero:
    print(f"No adivinaste. El número era {numero}.")
