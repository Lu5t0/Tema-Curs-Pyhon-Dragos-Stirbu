text = input("Scrie o propozitie aici:")
cuvant_cheie = "Python"
text2 = text.split(" ")
if cuvant_cheie in text2[0]:
    print(True)
else:
    print(False)