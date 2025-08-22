class Vehicule:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicule):
    def __init__(self, brand, year,seats):
        super().__init__(brand, year)
        self.seats = seats
class ElectricCar(Car):
    def __init__(self, brand, year,seats, battery_capacity, consum_pe_100_km):
        super().__init__(brand, year, seats)
        self.battery_capacity = battery_capacity
        self.consum_pe_100_km = consum_pe_100_km
    def calculare_autonomie(self):
        if self.battery_capacity > 0:
            return self.battery_capacity / self.consum_pe_100_km * 100
        else:
            return 0
    def info(self):
        autonomie = self.calculare_autonomie()
        return(f"Masina electrica: {self.brand}, An: {self.year}, Locuri: {self.seats},"
               f"Baterie: {self.battery_capacity} KWH, Consul: {self.consum_pe_100_km} KWH/100 KM,"
               f"Autonomie: {autonomie} KM")





if __name__ == "__main__":
    Ecar = ElectricCar("Tesla", 2022, 5, 68, 17)
    print(Ecar.info())


