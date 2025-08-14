# s = list("pptthhh")
s = list("xyyyzzz")
# s = list("ppttthhh")
frecvente = {}

for char in s:
    if char in frecvente:
        frecvente[char] += 1
    else:
        frecvente[char] = 1

poate = False

for i in range(len(s)):
    caracter = s[i]
    frec_copy = frecvente.copy()
    frec_copy[caracter] -= 1
    if frec_copy[caracter] == 0:
        del frec_copy[caracter]
    frec_set = set(frec_copy.values())
    if len(frec_set) == 1:
        poate = True
        break


if poate:
    print("Se poate")
else:
    print("Nu se poate")

