# My labs of my PCEP-30-0x certificacion in Cisco 🤖

# Scenario: Apple Counting in Python
# John had 3 apples.
# Mary had 5 apples.
# Adam had 6 apples.

# Variable assignment
john = 3
mary = 5
adam = 6

# Print individual values separated by comma
print(john, mary, adam, sep=', ')

# Calculate total apples
total_apples = john + mary + adam

# Print the total
print("Total number of apples:", total_apples)
----------------------------------------------------
# Ejemplo del uso de los parámetros sep y end en print()

# El separador "sep" define qué se coloca entre cada argumento
# El parámetro "end" define qué se imprime al final de la línea

print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# Salida esperada:
# Programming***Essentials***in...Python
----------------------------------------------------
# Ejemplo de uso de comillas dobles dentro de cadenas usando comillas escapadas (\") y saltos de línea (\n)

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

# Salida esperada:
# "I'm"
# ""learning""
# """Python"""
----------------------------------------------------
# Conversión entre millas y kilómetros
# 1 milla = 1.61 kilómetros

# Datos iniciales
kilometers = 12.25
miles = 7.38

# Conversión de millas a kilómetros
miles_to_kilometers = 7.38 * 1.61

# Conversión de kilómetros a millas
kilometers_to_miles = 12.25 * 0.621371

# Mostrar resultados redondeados a 2 decimales
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Salida esperada:
# 7.38 miles is 11.88 kilometers
# 12.25 kilometers is 7.61 miles
----------------------------------------------------
# Programa para calcular el cuadrado (potencia de 2) de un número introducido por el usuario

# Solicita un número al usuario y lo convierte a tipo float
anything = float(input("Enter a number: "))

# Eleva el número al cuadrado (potencia de 2)
something = anything ** 2.0

# Muestra el resultado en consola
print(anything, "to the power of 2 is", something)

# Ejemplo de salida:
# Enter a number: 3
# 3.0 to the power of 2 is 9.0
----------------------------------------------------
# Comparación simple: verificar si un número ingresado es mayor o igual a 100

# Solicita al usuario que ingrese un número entero
n = int(input("Enter a number: "))

# Verifica si el número es mayor o igual a 100
# Imprime True si lo es, False si no
print(n >= 100)

# Ejemplo de ejecución:
# Input: 30
# Output: False
----------------------------------------------------
# Programa que eleva un número ingresado por el usuario al cuadrado (potencia de 2)

# Solicita un número (float) al usuario
anything = float(input("Enter a number: "))

# Calcula el cuadrado del número usando el operador de potencia **
something = anything ** 2.0

# Muestra el resultado
print(anything, "to the power of 2 is", something)

# Ejemplo de ejecución:
# Enter a number: 3
# 3.0 to the power of 2 is 9.0
----------------------------------------------------
# Programa para encontrar el número mayor entre dos ingresados por el usuario

# Leer dos números desde el teclado
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Elegir el número mayor
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Mostrar el resultado
print("The larger number is:", larger_number)
----------------------------------------------------
# Programa que responde de forma diferente según cómo el usuario escriba "Spathiphyllum"

# Solicita al usuario el nombre de una flor
name = input("Enter flower name: ")

# Compara la entrada con diferentes variantes
if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")
----------------------------------------------------
# Programa para determinar si un año es bisiesto o común según el calendario gregoriano

# Solicita al usuario el año
year = int(input("Enter a year: "))

# Verifica si está dentro del periodo del calendario gregoriano
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Lógica para determinar si es un año bisiesto o común
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
