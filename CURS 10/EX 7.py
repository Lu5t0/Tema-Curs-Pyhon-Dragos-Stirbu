from traceback import print_tb


def scor_max(nume):
    abc = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17,
           "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
    def nume_scor_max(num):
        return sum(abc.get(char.lower(), 0) for char in num)
    for num in nume:
        print(f"{num} -> {nume_scor_max(num)}")



    return max(nume, key= nume_scor_max)

if __name__ == '__main__':
    print(scor_max(["mama", "tata", "Andrei", "Vlad"]))
