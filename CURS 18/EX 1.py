class Vehicule:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
class Car(Vehicule):
    def __init__(self,brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats
    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}")

class Bike(Vehicule):
    def __init__(self,brand, year, speeds):
        super().__init__(brand, year)
        self.speeds = speeds

    def display_info(self):
        super().display_info()
        print(f"Speeds: {self.speeds}")




if __name__ == "__main__":
    bike = Bike("Enduro", 2019, 12)
    car = Car("BMW", 2022, 5)

    print("Car info:")
    car.display_info()

    print("\nBike info:")
    bike.display_info()
