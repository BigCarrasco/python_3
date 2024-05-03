def lovefunc( flower1, flower2 ):
    # Compare the remainders of flower1 and flower2 when divided by 2
    if flower1 % 2 == flower2 % 2:
        # If the remainders are equal, it means both are even or both are odd,
        # which doesn't meet the "love" condition
        return False # They are not "compatible"
    else:
        # If the remainders are different, it means one is even and the other is odd,
        # which meets the "love" condition
        return True # They are "compatible"
    
        
#Test cases:
print(lovefunc(2,1)) # there is different each other so they are soultmates
print(lovefunc(2,2)) 
print(lovefunc(3,1))
print(lovefunc(10,2))



'''
Timmy & Sarah think they are in love, but around where they live, 
they will only know once they pick a flower each. If one of the flowers 
has an even number of petals and the other has an odd number of petals 
it means they are in love.

Write a function that will take the number of petals 
of each flower and return true if they are in love and false if they aren't.
'''