# 2. Write a program that collects two strings from a user, inserts them into a string
# "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string

response_one = input("Enter an object: ")
response_two = input("Enter a person: ")

output = "Yesterday I wrote a {}. I sent it to {}!".format(response_one, response_two)

print(output)
