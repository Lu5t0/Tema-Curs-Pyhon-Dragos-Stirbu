# Decorator pentru repetarea funcției
# Creează un decorator care apelează funcția decorată de 3 ori.

def repetare_de_3_ori(f):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            f(*args, **kwargs)

    return wrapper

@repetare_de_3_ori
def salut(nume):
    print(f"Salut: {nume}!")

if __name__ == '__main__':
    salut("Alex")
