import csv
with open('C:/Users/13768/Desktop/information.csv', 'r') as csvfile:
    i1 = 6
    q = []
    reader = csv.reader(csvfile)
    while i1 < 10:
        for row in reader:
            print(row)
    print(q)