from itertools import count

exemplu = [3, 7, 8, 5]
rezultat = []
for i in exemplu:
    calcul = sum(1 for x in exemplu if i > x)
    rezultat.append((i, calcul))
print("Ficare element este mai mare decat alte elemente de cate ori:")
for element, nr in rezultat:
    print(f"{element} -> {nr}")












