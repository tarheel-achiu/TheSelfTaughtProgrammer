input_1 = input("Enter string to convert to float ")

def convert_string_to_float(string):
    return float(string)

try:
    output_1 = convert_string_to_float(input_1)
    print(output_1)

except ValueError:
    print("Invalid input, enter integer ")
