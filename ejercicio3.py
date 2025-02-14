def convertir_a_romano(num):
    enteros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numero_convertido = ''
    for i in range(len(enteros)):
        while num >= enteros[i]:
            numero_convertido += romanos[i]
            num -= enteros[i]
    return numero_convertido

print(convertir_a_romano(2459))