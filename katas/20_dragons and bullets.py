'''
Instructions:
A hero is on his way to the castle to complete his mission. 
However, he's been told that the castle is surrounded with a couple of powerful 
dragons!.

each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets 
he should carry.. Assuming he's gonna grab a specific given number of bullets and 
move forward to fight another specific given number of dragons, will he survive?

Return true if yes, false otherwise :)

'''
def hero(bullets, dragons):
    bullets_need = dragons * 2
    
    if bullets >= bullets_need:
        return True
    else:
        return False
    
'''###test cases ###

        hero(7, 4) -> False
        hero(4, 5) -> False
        hero(100, 40) -> True
        hero(1500, 751) -> False
        
'''