cuvant = set(input("Scrie un cuvant:").upper())
consoane = {"B", "C", "D", "F", "H", "G", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z", "Y"}

consoane_cuvant = set(cuvant & consoane)
print(consoane_cuvant)
