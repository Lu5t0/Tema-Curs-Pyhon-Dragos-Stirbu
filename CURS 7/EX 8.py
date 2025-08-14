cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}
sub_pret = {}
pret_ron = {}
for car, pret in cars.items():
    if pret < 40000:
        sub_pret[car] = pret
print(sub_pret)
for car, ron in cars.items():
    pret_ron[car] = int(ron * 5.08)
print(pret_ron)

