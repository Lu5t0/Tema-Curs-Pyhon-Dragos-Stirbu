mesaj = (input("Scrie aici un mesaj:"))

try:
    print(float(mesaj))
except ValueError:
    print("Nu e numar")