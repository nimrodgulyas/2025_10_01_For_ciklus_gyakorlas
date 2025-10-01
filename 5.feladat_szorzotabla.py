"""
5. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

"""

szam = int(input('Adj meg egy számot!: '))

for i in range(11):
    print(szam, "x", i, "=", i*szam)