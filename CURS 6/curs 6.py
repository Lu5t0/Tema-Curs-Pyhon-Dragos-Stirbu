
list1 = [7, 2, 9, [2, 30], "Catalin", 5, 10.12, None]
lista2 = []
for i in list1:
    if type(i) == int or type(i) == float:
        lista2.append(i)
print(lista2)

if len(lista2) == 0:
    print("Nu exista numere!")
else:
    print(max(lista2))


