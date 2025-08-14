numbers = [1, 2, 3, 100, 200, 300]
# result = {1: False, 2: False, 3: False, 100: True, 200: True, 300: True}
mai_mare = {numar: numar > 10 for numar in numbers }
print(mai_mare)