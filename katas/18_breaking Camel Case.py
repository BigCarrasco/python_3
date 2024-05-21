def solution(s):
    resultado = ""
    for letra in s:
        if letra.isupper():
            resultado += " "
        resultado += letra
    return resultado.strip()
'''
#results

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''