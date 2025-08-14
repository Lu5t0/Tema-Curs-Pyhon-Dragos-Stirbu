prop = input("Scrie aici o propozitie:")
prop2 = prop.split(" ")
rez =  []


for cuvant in prop2:
    if  cuvant.lower()[0] != "a":
        rez.append(cuvant)

print(" ".join(rez))
