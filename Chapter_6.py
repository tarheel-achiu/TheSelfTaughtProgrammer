# 1. Print every character in the string "Camus".
#best way, iterate over the whole string

string_1 = "Camus"
for character in string_1:
    print(character)

#using idex and iteration variable
string_1 = "Camus"
for idx in range(5):
    print(string_1[idx])


#using custom index and no iteration variable
string_1 = "Camus"
idx = 0
for _ in range(5):
    print(string_1[idx])
    idx += 1


# 3. Use a method to make the string "aldous Huxley was born in 1894."
# grammatically correct by capitalizing the first letter in the sentence.

string = "aldous Huxley was born in 1894"

new_string = string.capitalize()




# 4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like:
# ["Where now?, "Who now?", WHen now?"]

string_1 = "Where now? Who now? When now?".split("?")
print(string_1)


# 5. Take the list [" The", "fox", "jumped", "over", "the", "fence", "."]
#and turn it into a grammatically correct string. There should be a space between each word,
#but no space between the word fence and the period that follows it.
#(Don't forget, you learned a method that turns a list of strings into a single string.)


list_1 = ["The", "fox", "jumped", "over", "the", "fence", "."]
string_1 = " ".join(list_1)
string_1 = string_1[0:29] + "." #could have beeen string_1[0:-2]
print(string_1)


# 6. Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign.

string_1 = "A screaming comes across the sky."
string_1 = string_1.replace("s", "$")
print(string_1)

# 7. Use a method to find the first index of the character "m" in the string "Hemingway".

"Hemingway".index("m")

# 10. Slice the string "It was a bright cold day in April, and the clocks were stricking thirteen." to only
# include the characters before the comma.

string_1 = "It was a bright cold day in April, and the clocks were stricking thirteen."
string_1[0:33]
