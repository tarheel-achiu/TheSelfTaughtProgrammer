# 1. Create a list of your favorite musicians.

musicians = ["Flume", "Galantis", "Childish Gambino", "Post Malone"]

# 2. Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited.

#   creating tuples
el_paso_tx = ("31.7619° N", "106.4850° W")

akron_oh = ("41.0814° N", "81.5190° W")

boston_ma = ("42.3601° N" , "71.0589° W")

chapel_hill_nc = ("35.9132° N", "79.0558° W")

san_francisco_ca = ("37.7749° N", "122.4194° W")

#   creating list
places_been = [el_paso_tx, akron_oh, boston_ma, chapel_hill_nc, san_francisco_ca]

print(places_been)

# 3. Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc.

my_attributes = {"height":
                 "5'8\"",
                 "favorite color":
                 "carolina blue",
                 "favorite author":
                 "Aldous Huxley",
                 "favorite sport":
                 "soccer"}

# 4. Write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the dictionary you created in the previous challenge.

my_attributes = {"height":
                 "5'8\"",
                 "favorite color":
                 "carolina blue",
                 "favorite author":
                 "Aldous Huxley",
                 "favorite sport":
                 "soccer"}

input_1 = input("Enter what you want to know about Andy; height, favorite color, favorite author, or favorite sport  ")

def stuff_about_andy(string):
    return my_attributes(string)

#try:
output_1 = stuff_about_andy(input_1)
print(output_1)

#except ValueError:
#    print("Invalid input, try again")

# 5. Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.

# 6. Lists, tuples, and dictioaries are just a few of the containers built into Python. Research python sets (a type of container). When would you use a set?
