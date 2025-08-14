
while True:
    numar_n = int(input("Scrie un numar natural:"))
    factorial = 1
    if numar_n == 0:
        print(f"{numar_n}! = 1")
        break
    else:
        multiplier = ""
        for i in range(1, numar_n + 1):
            factorial *= i
            multiplier += str(i)
            if i <  numar_n:
                multiplier += " * "
        print(f"{numar_n}! = {multiplier} = {factorial}")
        break





