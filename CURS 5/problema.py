# numar = 25
# while True:
#     numarul2 = int(input("Enter a number: "))
#     if numarul2 < numar:
#         print(f"Numarul este mai mare decat {numarul2}!")
#     elif numarul2 > numar:
#         print(f"Numarul este mai mic decat {numarul2}!")
#     else:
#         print("Ai castigat!")
#         break


text = input("Scrie un text aici:")
vocale = "aeiouAEIOU"
count_vocale = 0
count_consoane = 0

for char in text:
    if char.lower() in vocale:
        count_vocale += 1
    elif char.lower() in "qwrtypsdfghjklzxcvbnm":
        count_consoane += 1
print(f"Avem {count_vocale} vocale si {count_consoane} consoane")


