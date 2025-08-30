# *Decorator pentru verificarea tipurilor
# Creează un decorator care verifică dacă toate argumentele unei funcții sunt de tip int. Dacă nu, afișează un mesaj de eroare și nu apelează funcția.


def verifica_tipuri_int(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            print("Eroare: Toate argumentele trebuie să fie de tip int!")
            return

        if not all(isinstance(value, int) for value in kwargs.values()):
            print("Eroare: Toate argumentele trebuie să fie de tip int!")
            return
        return func(*args, **kwargs)
    return wrapper

@verifica_tipuri_int
def adunare(a, b):
    return a + b

if __name__ == '__main__':
    verficare = verifica_tipuri_int(adunare)
    print(verficare(1, 2))
    print(verficare(1,"2"))