liczby = []
c = 0
z1 = 0
z2 = 0
with open("liczby_60.txt", "r") as file:
    for line in file:
        num = int(line)
        if num < 1000:
            c+=1
            z1=z2
            z2=num
        liczby.append(num)
        listaDzielnikow = []
        for i in range(1, int(num**.05)):
            if num % i == 0:
                listaDzielnikow.append(i)
                listaDzielnikow.append(num//i)
            if num % num**0.5 == 0:
                listaDzielnikow.append(num**0.5)
            if len(listaDzielnikow) == 18:
                listaDzielnikow.sort()
                print(num, listaDzielnikow)

print(liczby, c, z1, z2)
