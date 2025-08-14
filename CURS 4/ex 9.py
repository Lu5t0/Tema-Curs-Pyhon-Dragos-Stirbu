mesaj = input("Scrie aici un mesaj:")
numar_spatii = mesaj.count(" ")
if numar_spatii < 1:
    print("Nu exista spatii in string-ul introdus.")
else:
    print(f"In total sunt {numar_spatii} spatii in mesaj.")