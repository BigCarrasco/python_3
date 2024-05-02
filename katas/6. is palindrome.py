'''
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the 
same backwards as forwards, such as madam or racecar.
'''

def palindrome(s):
    converted = s.lower()
    reverse = converted[::-1]
    print(reverse)
    if converted == reverse:
        return True
    else:
        return False