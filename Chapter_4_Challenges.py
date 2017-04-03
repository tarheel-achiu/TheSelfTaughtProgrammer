#Challange #1
def squared(x):
    """
    Returns x^2.
    :param x: int.
    :return: int square of x.
    """
    return x**2

print (squared(2))

#Challange #2

def print_string(string):
    print(string)

print_string("Hello, World!")

#Challange #3

def add_five_int(req1, req2, req3, op1 = 1, op2 = 2):
    return req1 + req2 + req3 + op1 + op2

print(add_five_int(1,2,3))

#Challange #4
input_1 = input("Enter integer to get divided by 2")

def divide_by_2(int1):
    return int1 / 2

def mult_by_four(int1):
    return int1 * 4

func1_output = divide_by_2(input_1)

func2_output = mult_by_four(func1_output)

print(func2_output)
