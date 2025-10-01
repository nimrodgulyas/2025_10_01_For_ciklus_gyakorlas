"""
2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.

"""
a = int(input("Add meg az első számot (a): "))
b = int(input("Add meg a második számot (b): "))
if a > b:
    for i in range(b+1,a):
        print(i)

elif a < b:
    for i in range(b-1,a,-1):
        print(i)
else:
    print("A két szám egyenlő, nincs köztük szám.")
