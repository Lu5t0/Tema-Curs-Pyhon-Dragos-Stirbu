# Decorator simplu de mesaj
# Creează un decorator care afișează un mesaj înainte și după apelarea unei funcții.


def hello_decorator(f):
    def wrapper(*args, **kwargs):
        print("Aici incepe functia.")
        rezultat = f(*args, **kwargs)
        print(rezultat)
        print("Aici se termina functia.")
        return rezultat

    return wrapper


def suma_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

if __name__ == "__main__":
    decorated_function = hello_decorator(suma_n)
    decorated_function(5)


