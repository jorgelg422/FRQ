import csv
def read():
    res = []
    with open('export.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            res.append(row)
    return res[971:1000]