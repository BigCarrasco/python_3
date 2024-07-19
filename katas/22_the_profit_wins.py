'''
I N S T R U C T I O N S
Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course,
this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. 
Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.
 
'''

def min_max(lst):
    min_num = min(lst)
    max_num = max(lst)
    arr = [min_num, max_num]
    return arr

'''R E F A C T O R '''
def min_max(lst):
    return [min(lst), max(lst)]

''' T E S T   C A S E S 
        min_max([1,2,3,4,5]), [1, 5])
        min_max([2334454,5]), [5, 2334454])

'''

