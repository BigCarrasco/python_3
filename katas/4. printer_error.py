import re 

def printer_error(s):
    contador = 0
    contador2 = 0
    x = re.findall(r"[n-z]",s)
    for i in x:
        contador += 1
 
    for y in s:
        contador2 += 1
     
    print(f'{contador}/{contador2}')

printer_error("rain in spain")
