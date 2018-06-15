import csv
import sys
from collections import OrderedDict

if __name__ == "__main__":
    f = open(sys.argv[1])
    reader = csv.reader(f)
    list = []
    for row in reader:
        list.append(row)
    list.pop(0)

    competitors = []
    for x in list:
        competitors.append(x[1])
    #print(list)

    competitors = sorted(set(competitors))
    #print("Competitors: " + str(competitors) + "\n")

    for x in competitors:
        print(x)
        for y in list:
            if x == y[1]:
                print("EVENT: " + y[0] + " GROUP: " + y[2])
        print()
