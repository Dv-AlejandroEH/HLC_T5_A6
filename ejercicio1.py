def calcular_pares (lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i
    return f"La suma de los números pares de la lista es igual a: {suma}"
print(calcular_pares([1, 2, 3, 4, 5, 6]))