def linii_in_ordine_inversa(input_file, output_file):
    with open(input_file, "r") as fisier:
        lines = fisier.readlines()
    lines_inversate = lines[::-1]
    with open(output_file, "w") as fisier:
        fisier.writelines(lines_inversate)
    with open(output_file, "r") as fisier:
        print(fisier.read())
if __name__ == "__main__":
    linii_in_ordine_inversa("input.txt", "output.txt")