import sys
import csv

# python csv-to-txt.py file.csv

filename = sys.argv[1].split(".")[0]
with open(sys.argv[1], 'r') as file_object:

    lines = csv.reader(file_object)

    with open(("{}.txt".format(filename)), 'w') as file_output:
        for line in lines:
            for item in line:
                print("{}".format(item), file=file_output)


# print('Hello', 'World', 2+3, file=open('file.txt', 'w'))
