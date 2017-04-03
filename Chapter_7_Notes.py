#For Loop

for [variable_name] in [iterable_name]:
    [instructions]

#where [variable_name] is a variable name of your choosing assigned to the value of each item in the iterable,
#and [instructions] is the code to be executed each time through the loop.

#For loop through iterable string

name = "Ted"
for character in name:
    print(character)

#For loop though iterable list

shows = ["GOT",
         "Narcos",
         "Vice"]

for show in shows:
    print(show)

#For loop though iterable tuple

coms = ("A. Development",
        "Friends",
        "Always Sunny")
for show in coms:
    print(show)

#For loop through iterable keys in dictonary

people = {"G. Bluth II": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"
          }

for character in people:
    print(character)

#For loop to change mutable iterable list

tv = ["GOT",
      "Narcos",
      "Vice"]

i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)


#For loop to change mutable iterable list - different syntax using enumerate

tv = ["GOT",
      "Narcos",
      "Vice"]

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

#For loop to move data between mutable iterables

tv = ["GOT",
      "Narcos",
      "Vice"]

coms = ["A. Development",
        "Friends",
        "Always Sunny"]

all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

#while loop

while [expression]:
    [code_to_execute]

#while loop, runs until x is no longer > 0

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1

print("Happy New Year!")

#using break statement to exit a while loop

qs = ["What is your name?",
      "What is your favorite color?",
      "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

#using continue statement in a for loop

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#using continue statement in a while loop

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#nested for loops

for i in range(1,3):
    print (i)
    for letter in ["a", "b", "c"]:
        print(letter)

#nested for loop to add all the numbers in one list to all the numbers in another list

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

#nested for loop in while loop

while input('y or n? ') != "n":
    for i in range(1, 6):
        print(i)
