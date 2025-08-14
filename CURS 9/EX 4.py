num = int(input("Scrie un numar de 4 cifre aici:"))
if 1000 <= num <= 9999:
    while True:
        num += 1
        if len(set(str(num))) == 4:
            print(num)
            break
else:
    print("Numarul introdus nu este de 4 cifre!")

