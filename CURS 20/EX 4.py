# Date două liste, una cu prenume și alta cu nume de familie, folosește map și lambda pentru a le combina într-o listă de nume complete
# (din ["Ion", "Maria", "Andrei"] si ["Popescu", "Ionescu", "Georgescu"] obtinem ["Ion Popescu", "Maria Ionescu", "Andrei Georgescu"]).

if __name__ == '__main__':

    Nume = ["Ion", "Maria", "Andrei"]
    Prenume = ["Popescu", "Ionescu", "George"]

    lista_nume = list(map(lambda x,y: x + " " + y, Nume, Prenume))
    print(lista_nume)

