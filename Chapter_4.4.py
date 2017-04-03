#Challange #4
input_1 = int(input("Enter integer to get divided by 2 then multiplied by 4: "))

def divide_by_2(int1):
    return int1 / 2

def mult_by_four(int1):
    return int1 * 4

func1_output = divide_by_2(input_1)

func2_output = mult_by_four(func1_output)

print(func2_output)
