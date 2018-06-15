import csv
import sys

if __name__ == "__main__":
    f = open(sys.argv[1])
    newF = open(sys.argv[2], "w+")
    reader = csv.reader(f)
    entries = []
    for row in reader:
        entries.append(row)
        entries.pop(0)

    competitors = []
    for x in entries:
        competitors.append(x[1])
    competitors = sorted(set(competitors))

    for x in competitors:
        print(x+",,")
        newF.write(x+",,"+"\n")
        newF.write("Event/Round,Stage/Group,\n")
        for y in entries:
            if x == y[1]:
                print(y[0] + "," + y[2] + ",")
                newF.write(y[0] + "," + y[2] + ",\n")
        print("\n")
        newF.write(",,")
        newF.write("\n")
