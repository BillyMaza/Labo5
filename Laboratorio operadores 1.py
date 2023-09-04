print("Billy Mazariegos Practica 1.")
nombre = input("Hola!, introduce tu nombre aqui: ")
print("Hola, " + nombre + "este es un programa que nos dirá tu IMC.")
peso = float(input("Por favor, introduce tu peso en kilogramos: "))
altura = float(input("Por favor, introduce tu altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obeso"

# Imprimir el resultado
print("Tu Índice de Masa Corporal (IMC) es:", imc)
print("Categoría de IMC:", categoria)
