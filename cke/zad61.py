ciagi = []
with open("ciagi.txt") as plik:
    for linia in plik:
        liczby=[]
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
            ciagi.append(liczby)

print(ciagi)
