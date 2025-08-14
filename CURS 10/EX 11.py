def sting_nou(text):
    text1 = text.split()
    lista_noua = []
    for char in range(len(text1)):
        if char == 0:
            lista_noua.append(text1[-1])
        elif char == len(text1) - 1:
            lista_noua.append(text1[0])
        else:
            lista_noua.append(text1[char])
    return " ".join(lista_noua)

if __name__ == "__main__":
    print(sting_nou("python java        javascript"))
    print(sting_nou("mere pere      mure"))
    print(sting_nou("Mihai Andrei        Ion"))