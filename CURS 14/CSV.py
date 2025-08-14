import csv

if __name__ == "__main__":
    with open("users.csv", ) as csvfile:
        csvreader = csv.reader(csvfile)
        # print(type(csvreader))
        next(csvreader)
        for row in csvreader:
            print(row)