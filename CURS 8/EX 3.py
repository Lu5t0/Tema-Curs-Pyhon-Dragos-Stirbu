cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}
pret_ron = {car: price * 5 for car, price in cars.items()}
print("Prețurile în RON:", pret_ron)

mai_scumpe = {car: price for car, price in cars.items() if price > 20000}
print("Mașinile mai scumpe de 20k EUR:", mai_scumpe)