import random

print("Üdv a Számháború játékban!")

nyer = 0
veszit = 0
dontetlen = 0

while True:
    while True:
            szam = int(input("Adj meg egy számot 1 és 6 között: "))
            if 1 <= szam <= 6:
                break
            else:
                print("Csak 1 és 6 közötti számot adhatsz meg!")
    
    gep_szam = random.randint(1, 6)
    print(f"A gép száma: {gep_szam}")

    if szam > gep_szam:
        print("Nyertél!")
        nyer += 1
    elif szam < gep_szam:
        print("Vesztettél!")
        veszit += 1
    else:
        print("Döntetlen!")
        dontetlen += 1
    ujra = input("Szeretnél újra játszani? (i/n): ")
    if ujra == 'n':
        print(f"Végső eredmény: {nyer} nyerés, {veszit} vereség, {dontetlen} döntetlen.")
        break
    elif ujra == 'i':
        print("Akkor hajrá!")
    else:
        print("Nem értem, de folytassuk akkor!")