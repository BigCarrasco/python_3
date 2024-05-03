'''
You are going to be given a word. Your job is to return the middle character of the word.

If the word's length is odd, return the middle character. 
If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
'''
def get_middle(s):
    index, odd = divmod(len(s), 2)
    print(s[index] if odd else s[index - 1:index + 1])

get_middle("test")
get_middle("testing")
get_middle("middle") 
get_middle("A") 