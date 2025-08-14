prop = input('Scrie o propozitie:')
cuvinte = prop.replace(" ", "")
litere = []
for char in cuvinte:
    if char in cuvinte and char not in litere:
        litere.append(char)

print(litere)