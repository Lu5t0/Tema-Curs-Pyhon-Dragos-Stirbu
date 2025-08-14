info_grades = {
    'Maria': [8, 9, 10],
    'Bogdan': [8.6, 7.3, 9.9, 10],
    'Ilinca': [10, 10],
    'Andra': [9.5, 7, 9],
    'Daniel': [6, 10, 9.7]
}
nr_note_3 = ()
medie = {}
for name, grade in info_grades.items():
    total_g = 0
    if len(grade) == 3:
        nr_note_3 += (name,)
    for i in grade:
        total_g += i
        avarage = total_g / len(grade)
        medie[name] = avarage
cea_mai_mare = max(medie.values())
for loc1, valoare_medie in medie.items():
        if valoare_medie == cea_mai_mare:
            nume_loc1 = loc1

print(f"Elevii care au  3 note sunt:{nr_note_3}")
print(f"Mediile elevilor sunt:{medie:}")
print(f"Cea mai mare medie este al lui {nume_loc1} cu media de {int(cea_mai_mare)}")



