print("Billy Mazariegos, practica 1")
usuario = input("Hola!, introduce tu nombre aqui: ")
print("Hola "+usuario+" danos los números que quieres ordenar, ")
numerosU = input("ingresandolos separados por un espacio, así no habran errores :) ")

numeros_como_cadenas = numerosU.split()

numeros = [int(numero) for numero in numeros_como_cadenas]

n = len(numeros)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if numeros[j] < numeros[min_index]:
            min_index = j
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]

print("Aquí esta tu lista ordenada:")
for numero in numeros:
    print(numero, end=" ")