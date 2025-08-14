lista = ["python", "java", "apa","verde" ]
lista2 = []
tot = 0
numar_str = 0
for element in lista:
    if isinstance(element, str):
        numar_str += 1
    tot += len(lista)
    medie = tot / numar_str
if len(lista[0]) > medie:
    lista2.append(lista[0])
if len(lista[1]) > medie:
    lista2.append(lista[1])
if len(lista[2]) > medie:
    lista2.append(lista[2])
if len(lista[3]) > medie:
    lista2.append(lista[3])

print(lista2)