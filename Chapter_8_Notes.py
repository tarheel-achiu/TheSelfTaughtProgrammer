# importing the built-in module and using it

import [module_name]

[module_name].[code]


#example using pow func and math module

import math

math.pow(2, 3)

#creating random numbers with random module

import random

random.randint(0, 100)

#calculate mean median and mode of an iterable of numebrs

import statistics

nums = [1, 5, 33, 12, 46, 33, 2]

# mean
statistics.mean(nums)

#median
statistics.median(nums)

#mode
statistics.mode(nums)


#using keyword module to check if string is a python keyword

import keyword

keyword.iskeyword("for")
keyword.iskeyword("football")

#how to prevent custom modules from running at import

if __name__=="__main__":
    [code]
