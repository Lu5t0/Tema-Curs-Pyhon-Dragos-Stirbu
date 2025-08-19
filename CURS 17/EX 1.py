# Clasa „Car”
# Creează o clasă Car cu atribute: brand, model, year.
# Adaugă o metodă display_info() care afișează informațiile despre mașină.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Car Brand:{self.brand} Model:{self.model} Year:{self.year}")


if __name__ == "__main__":
    car = Car("BMW", 2019, 12)
    car.display_info()
