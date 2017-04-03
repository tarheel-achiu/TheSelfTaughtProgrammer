#using os module to create correctly formated file path

import os
os.path.join("Users",
             "bob",
             "st.txt")
#using the python open function, first para: file path as a string and second para: mode as a string

"r" : "open a file for reading only"
"w" : "open a file for writing only, overwrites exsiting file, or creates on if it does not exsist"
"w+" : "open a file for reading and writing, overwrites exsiting file, or creates on if it does not exsist"

[file_object] = open("[file_path]","[mode]")

#example for opening a file, writing to it, and closing

file_object = open("file.txt", "w")
file_object.write("Hi, from Python!")
file_object.close()

#syntax to automatically close files using with statement

with open([file_path], [mode]) as [variable_name]:
    [variable_name].[module]

#example

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

#you can only read a file once, other wise you have to close and re-open it
#to get around this you can assigne the contents of the folder to a varable such as a list

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)


#writing as a csv files

import csv

with open("st.txt","w") as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])


#reading from a csv file

import csv


with open("st.txt", "r") as f:
    r = csv.reader(f, delimiter=",")

    for row in r:
        print(",".join(row))
