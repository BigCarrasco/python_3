def count_sheep(n):
    resultado = ""
    if n == 0:
        return resultado
    for x in range(n+1):
        if x > 0:
            resultado += f"{x} sheep..."
    return resultado
        
        
###Refactor
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

''' test cases for:

        count_sheep(0) -> ""
        count_sheep(1) -> "1 sheep...");
        count_sheep(2) -> "1 sheep...2 sheep...")
        count_sheep(3) -> "1 sheep...2 sheep...3 sheep...")
'''
