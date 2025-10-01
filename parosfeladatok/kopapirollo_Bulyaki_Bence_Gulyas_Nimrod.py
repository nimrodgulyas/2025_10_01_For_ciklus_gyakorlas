print('Üdvözlünk a kő, papír, olló játékunkban! A mai napon a játékmestereink: Bulyáki Bence Benedikt és Gulyás Nimród! Sok sikert!')


1 == 'kő'
2 == 'papír'
3 == 'olló'


nyer = 0
veszit = 0
dontetlen = 0

while True:
    x = int(input('Kő(1), papír(2) vagy olló(3)?: '))
    import random
    y = random.randint(1,3)
    if x == 1 and y == 1 or x == 2 and y == 2 or x == 3 and y == 3:
        print('Döntetlen!')
        dontetlen += 1
    if x == 1 and y == 3 or x == 3 and y == 2 or x == 2 and y == 1:
        print('Bravóóóóóóóóóóó! Nyertél!')
        nyer += 1
    if x == 1 and y == 2 or x == 2 and y == 3 or x == 3 and y == 1:
        print('Hahahahaha, vesztettél!')
        veszit += 1
    z = str(input('Szeretnél még játszani?: '))
    if z == 'nem':
        print(f'Játék vége! Az eredményeitek: Győztes játék: {nyer}, Elveszített játék: {veszit}, Döntetlen játék: {dontetlen} ')
        break
    elif z == 'igen':
        print('Akkor hajrá!')
    else:
        print('Nem értem amit írsz de akkor folytassuk!:)')

