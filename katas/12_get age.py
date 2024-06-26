'''
You ask a small girl,"How old are you?" She always says, "x years old", 
where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, 
the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

'''

def get_age(age):
    return int(age[0])

get_age("2 years old") #return 2
get_age("4 years old") #return 4
get_age("5 years old") #return 5
get_age("7 years old") #return 7