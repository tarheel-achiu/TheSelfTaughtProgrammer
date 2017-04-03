# 1.print each item in the followin list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diares"].

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diares"]

for i in shows:
    print(i)

# 2. Print all the numbers from 25 to 50

for i in range(25, 51):
    print(i)

# 3. Print each item from the first challenge and their indexes

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diares"]

ind = 0
for i in shows:
    print(i,ind)
    ind += 1

#another way

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(shows):
    print(show, index)

#Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers on the list and tell them whether or not they guessed correctly

numbers = [5,7,3]

while True:
    answer = input("Guess a number or type q to quit. ")
    if answer == "q":
        break
    try:
         answer = int(answer)
    except ValueError:
        print("please type a number or q to quit. ")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
