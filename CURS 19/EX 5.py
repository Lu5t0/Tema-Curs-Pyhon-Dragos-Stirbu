class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9



if __name__ == "__main__":
    c = 20
    f = 90

    print(f"{c} grade celsus = {TemperatureConverter.celsius_to_fahrenheit(c):.2f} grade fahrenheit")
    print(f"{f} grade fahrenheit = {TemperatureConverter.fahrenheit_to_celsius(f):.2f} grade celsus ")