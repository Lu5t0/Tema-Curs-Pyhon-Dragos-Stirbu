import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator can't be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den =self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator} / {self.denominator}"


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
