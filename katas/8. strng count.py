'''

Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
str_count("Hello", 'o'); // returns 1
str_count("Hello", 'l'); // returns 2
str_count("", 'z'); // returns 0

'''

def str_count(strng, letter):
    variable = []
    for x in range(len(strng)):
        if strng[x] == letter:
            variable += strng[x]
    return variable.count(letter)
   