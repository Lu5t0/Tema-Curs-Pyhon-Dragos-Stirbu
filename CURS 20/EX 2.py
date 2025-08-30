# Lungimea cuvintelor
# Dată o listă de cuvinte, folosește map și lambda pentru a obține lungimea fiecărui cuvânt.

if __name__ == '__main__':
    lista1 = ["mihai", "andrei", "alex"]

    nr_litere = list(map(lambda x: len(x), lista1))
    print(nr_litere)