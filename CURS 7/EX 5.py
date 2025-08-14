numbers = [1, 1, 3, 7, 9, 2, 3, 100, 9, 333, 2.0, 5, 1, 3, 3]
numaratori = {}
for numar in numbers:
    if isinstance(numar, (int, float)):
        if numar not in numaratori:
            numaratori[numar] = 1
        else:
            numaratori[numar] += 1

print(numaratori)