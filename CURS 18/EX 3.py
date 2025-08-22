class Animal:
    def make_sound(self):
        print("Animal's sound")

class Dog(Animal):
    def make_sound(self):
        print("Ham Ham")

class Cat(Animal):
    def make_sound(self):
        print("Miau Miau")

class Cow(Animal):
    def make_sound(self):
        print("Muu Muu")

if __name__ == "__main__":
   animals = [Dog(), Cat(), Cow(), Dog(), Cat(), Cow()]

   for animal in animals:
       animal.make_sound()
