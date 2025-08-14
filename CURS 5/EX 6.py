string1 = input("Scrie un text: ")
cuvinte1 = string1.replace(" ", "")
string2 = input("Scrie alt text: ")
cuvinte2 = string2.replace(" ", "")
caractere_com = 0
caractere = []
for char in cuvinte1:
    if char  in cuvinte2:
        caractere_com += 1

for caracter in cuvinte1:
    if caracter in cuvinte2 and caracter not  in caractere:
        caractere.append(caracter)
print(caractere_com)
print(caractere)



