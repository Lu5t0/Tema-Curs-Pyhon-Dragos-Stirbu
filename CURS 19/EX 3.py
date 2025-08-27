class BankAccount:
    def __init__(self,nume, sold):
        self.nume = nume
        self.sold = sold
    def __str__(self):
        return f"Nume cont:{self.nume}, sold:{self.sold}"

    def __eq__(self, other):
        return self.sold == other.sold

    def __lt__(self, other):
        return self.sold < other.sold




if __name__ == '__main__':
    account1 = BankAccount("Mihai", 500)
    account2 = BankAccount("Andrei", 700)
    account3 = BankAccount("Jim", 600)
    account4 = BankAccount("Alex", 500)
    conturi = [account1, account2, account3]

    print(f"{account1.__str__()} are soldul egal cu {account2.__str__()}:", account1 == account2)
    print(f"{account1.__str__()} are soldul egal cu {account4.__str__()}:", account1 == account4)
    conturi_sortate= sorted(conturi)
    print("Conturi sortate crescator:")
    for cont in conturi_sortate:
        print(cont)


