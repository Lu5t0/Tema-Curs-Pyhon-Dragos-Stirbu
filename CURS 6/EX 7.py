words = ["python", "ruby", "javascript"]
cuvant_inversat = ""
cuvant_inversat2 = ""
cuvant_inversat3 = ""
words_fin = []
for world in words[0]:
    cuvant_inversat = world + cuvant_inversat
words_fin.append(cuvant_inversat)
for world in words[1]:
    cuvant_inversat2 = world + cuvant_inversat2
words_fin.append(cuvant_inversat2)
for world in words[2]:
    cuvant_inversat3 = world + cuvant_inversat3
words_fin.append(cuvant_inversat3)

print(words_fin)