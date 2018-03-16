import sys
import csv

# in command line
# python csv-to-md.py file.csv

filename = sys.argv[1].split(".")[0]
with open(sys.argv[1], 'r') as file_object:

    lines = csv.reader(file_object)

    with open(("{}.md".format(filename)), 'w') as file_output:
        for line in lines:
            if len(line[0]) == 0:
                print("\n", file=file_output)
            elif len(line[1]) == 0:
                print("## {}".format(line[0]), file=file_output)
                print("step | syntax", file=file_output)
                print(" --- | --- ", file=file_output)
            else:
                for item in line:
                    if len(item) > 0:
                        if item[0].isupper():
                            print(item, end=" | ", file=file_output)
                        else:
                            print("`{}`".format(item), file=file_output)
