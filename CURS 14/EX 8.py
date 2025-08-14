import csv
def citeste_clienti(inp_client):
    clienti = {}
    with open(inp_client, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            id_client = row['id_client']
            nume = row['nume_client']
            clienti[id_client] = nume
    return clienti

def creaza_raport(clienti,input_comenzi,raport):
    comenzi = []
    with open(input_comenzi, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            id_comanda = row['id_comanda']
            id_client = row['id_client']
            suma = row['suma']
            data = row['data']
            nume_client = clienti.get(id_client, "Necunoscut")
            comenzi.append({
                "id_comanda": id_comanda,
                "nume_client": nume_client,
                "suma": suma,
                "data": data,
            })
    with open(raport,"w", newline='') as csvfile:
        fieldnames = ['id_comanda', 'nume_client', 'suma', 'data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comenzi)


if __name__ == "__main__":
    creaza_raport(citeste_clienti("clienti.csv"),"comenzi.csv","raport.csv" )

