def safe_divide(a, b):
    try:
        rezultat = a / b
    except ZeroDivisionError:
        print("Impartire la zero interzisa!")
    except TypeError:
        print("Valori invalide!")
    except Exception as e:
        print(f"A aparut o eroare neasteptata:{e}")
    else:
        return rezultat

if __name__ == "__main__":
    print(safe_divide(100, 0))
    print(safe_divide("100", "1"))
    print(safe_divide(100, 5))