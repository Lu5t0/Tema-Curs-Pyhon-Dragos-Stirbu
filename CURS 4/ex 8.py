from traceback import print_tb

mesaj = input("Scrie un mesaj aici:")

sectiuni = mesaj.split(".")
if len(sectiuni) == 1 and sectiuni[0].isdigit():
    patrat = int(mesaj) ** 2
    print(patrat)
elif len(sectiuni) == 2 and sectiuni[0].isdigit() and sectiuni[1].isdigit():
    patrat = float(mesaj) ** 2
    print(patrat)
else:
    print(mesaj)






