"""
1. Összegszámítás
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.

"""

x = int(input("Írj be egy egész számot!: "))
y = 0
for i in range(x):
    y += i
print(f' {y}')