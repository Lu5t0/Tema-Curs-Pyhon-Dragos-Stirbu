# Transformare în majuscule
# Dată o listă de șiruri de caractere (toate cu litere mici), folosește map și lambda pentru a le transforma în litere mari.

if __name__ == "__main__":

    lista1 = ["mihai","andrei","alex"]

    majuscule = list(map(lambda x: x.upper(), lista1))
    print(majuscule)