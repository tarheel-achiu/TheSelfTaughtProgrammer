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
    return my_attributes[string]

if input_1 in my_attributes:

# unnessary since the if statment won't go if there is no match
    try:
        output_1 = stuff_about_andy(input_1)
        print(output_1)

    except KeyError:
        print("Invalid input, try again")

else: 
    print("Invalid input, try again")
