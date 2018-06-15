import csv
import sys

if __name__ == "__main__":
    #Declare files from args, read in from input
    f = open(sys.argv[1] +".csv")
    newF = open(sys.argv[2] +".csv", "w+")
    reader = csv.reader(f)
    entries = []
    for row in reader:
        entries.append(row)
    entries.pop(0)

    #Create list of competitors
    competitors = []
    for x in entries:
        competitors.append(x[1])
    competitors = sorted(set(competitors))
    print(competitors)

    #Per competitor, list their events followed by their stage and group
    for x in competitors:
        print(x+",,")
        newF.write(x+",,"+"\n")
        newF.write("Event/Round,Stage/Group,\n")
        for y in entries:
            if x == y[1]:
                print(y[0] + "," + y[2] + ",")
                newF.write(y[0] + "," + y[2] + ",\n")
        print(",,")
        newF.write(",,")
        newF.write("\n")
