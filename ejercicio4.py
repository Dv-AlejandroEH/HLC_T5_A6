def comprobar_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return comprobar_palindromo(palabra[1:-1])

print(comprobar_palindromo(''))
print(comprobar_palindromo('radar'))
print(comprobar_palindromo('hello'))