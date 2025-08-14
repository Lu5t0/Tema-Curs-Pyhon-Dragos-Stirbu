verde = 3
rosu = 2

timp_total = rosu + verde
timp_necunoscut = int(input("Scrie minutul aici:"))
positie_in_ciclu = timp_necunoscut % timp_total

if timp_necunoscut < 0:
    print("Timpul nu poate fi negativ")
elif timp_necunoscut > 60:
    print("Nu pot fi mai mult de 60 de minute.")
elif 0 < positie_in_ciclu <= 3:
    print(f"Semaforul la minutul {timp_necunoscut} este Verde")
else:
    print(f"Semaforul la minutul {timp_necunoscut} este Rosu")







