"""
3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.

"""

jojelszo = 'siker'
while True:
    jelszo = input('Add meg a jelszavad!: ')
    if jelszo == jojelszo:
            print('A jelszó helyes!')
            break
    else:
        print('A jelszó nem jó!')