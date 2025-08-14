import numbers

numere_disponibile = {str(i) for i in range(1, 50)}

numere_trase = set()
for i in range(6):
    numere_trase.add(int(numere_disponibile.pop()))
raspuns = list(numere_trase)
raspuns.sort()

print(raspuns)



# tuplu = tuple((numar, "test") for numar in numere_disponibile)
# set_Extragere = set(tuplu)
#
# print(set_Extragere.pop)




