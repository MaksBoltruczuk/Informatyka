def horner(liczba, x):
    w = int(liczba[0])
    for i in range(1, len(liczba)):
        w = x * w + int(liczba[i])
    return w


ciagi = []

with open("ciagi.txt") as file:
    for linia in file:
        ciagi.append(linia.strip())

for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])


licznik = 0
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik += 1


liczby = []

for i in range(len(ciagi)):
    liczby.append(horner(ciagi[i], 2))

sito = []

for i in range(363000):
    sito.append(1)

for i in range(2, 363000):
    if sito[i] == 1:
        for j in range(i+i, 363000, i):
            sito[j] = 0

pierwsze = []

for i in range(2, 363000):
    if sito[i] == 1:
        pierwsze.append(i)

for i in range(len(liczby)):
    czynniki = []
    for j in range(len(pierwsze)):
        liczba = liczby[i]
        while liczba % pierwsze[j] == 0:
            czynniki.append(pierwsze[j])
            liczba = liczba // pierwsze[j]
            if len(czynniki) > 2:
                break
    if len(czynniki) == 2:
        print(liczby[i], czynniki)
