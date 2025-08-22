class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f'Nume:{self.name}, Salariu: {self.salary} EURO'

class Developer(Employee):
    def __init__(self, name, salary,limbaj_de_prog):
        super().__init__(name, salary)
        self.limbaj_de_prog = limbaj_de_prog

    def __str__(self):
        return f"{Employee.__str__(self)}, Cunostinte in programare: {self.limbaj_de_prog}"

class Designer(Employee):
    def __init__(self, name, salary,soft_de_design):
        super().__init__(name, salary)
        self.soft_de_design = soft_de_design

    def __str__(self):
        return f"{Employee.__str__(self)}, Cunostinte in design: {self.soft_de_design}"


if __name__ == "__main__":
    angajat = Developer("Mihai", 5000, "Python")
    agajat2 = Designer("Andrei", 5500, "Canva")

    print(angajat)
    print(agajat2)






