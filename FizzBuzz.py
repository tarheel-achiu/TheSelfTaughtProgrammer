# FizzBuzz interview question
# Write a program that prints the numbers from 1 to 100.
# But for nultipules of three print "Fizz" instead of the number,
# and for the multples of five print "Buzz." For multiples of
# both three and five print "FizzBuzz"

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 \
         and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 ==0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()
