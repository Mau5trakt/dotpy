import random
Secuencia = []
for i in range(10):
    if i < 2:
        Aleatorio = random.randint(1,6)
        Secuencia.append(Aleatorio)
    else:
        Aleatorio = random.randint(1,6)
        while Aleatorio == Secuencia[i-1] and Aleatorio == Secuencia[i-2]:
            Aleatorio = random.randint(1,6)

        Secuencia.append(Aleatorio)

print(Secuencia)