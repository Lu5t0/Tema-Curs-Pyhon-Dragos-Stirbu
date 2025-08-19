class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Angajat: {self.name}, Salariu: {self.salary}"

class Manager(Employee):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.angajati = []
    def add_employee(self,employee):
        if isinstance(employee,Employee):
            self.angajati.append(employee)
    def show_subordinates(self):
        if not self.angajati:
            print(f"{self.name} nu are angajati in subordine.")
        else:
            print(f"Angajatii coordonati de {self.name}:")
            for emp in self.angajati:
                print(f"-{emp.name}")
    def __str__(self):
        return f"Manager: {self.name}, Salariu: {self.salary} RON, Nr. subordonati: {len(self.angajati)}"

if __name__ == "__main__":
    angajat1 = Employee("Mihai Ionescu", 5000)
    angajat2 = Employee("Ana Popescu", 7000)

    manager1 = Manager("Andrei Popa", 9000)
    manager1.add_employee(angajat1)
    manager1.add_employee(angajat2)
    print(manager1)
    manager1.show_subordinates()
