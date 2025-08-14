import time


def list_append(numar):
    start = time.time()
    lista_char = []
    for i in range(numar):
        lista_char.append(i)
    end = time.time()
    return end - start

def list_compre(numar):
    start = time.time()
    lista_char = [i for i in range(numar)]
    end = time.time()
    return end - start

if __name__ == '__main__':
    numar = 5_000_000
    print("Timp cu append", list_append(numar))
    print("Timp cu comprehension", list_compre(numar))
