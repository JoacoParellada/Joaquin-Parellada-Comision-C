
from tp5_funciones import validation_dni
#ejercicio.1
"""

dni=input("Ingrese su DNI: ")
result = validation_dni(dni)
print(result)

#ejercicio.2
from tp5_funciones import long_last_word

phrase = input("Ingrese una frase: ")
result = long_last_word(phrase)
print("La longitud de la ultima palabra de la frase es: ",result)

#ejercicio.3

from tp5_funciones import generate_id

#ejercicio.4
from tp5_funciones import is_multiple

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if is_multiple(n1,n2):
    print(f"{n1} es multiplo de {n2}")
elif is_multiple(n2,n1):
    print(f"{n2} es multiplo de {n1}")
else:
    print("Ninguno numero es multiplo del otro.")

#ejercicio.5
from tp5_funciones import medium_temperature

days = int(input("Ingrese el numero de dias: "))
med_temp = []

for i in range(days):
    temp_max = float(input(f"Ingrese la temperatura maxima del dia {i+1}: "))
    temp_min = float(input(f"Ingrese la temperatura minima del dia {i+1}: "))
    midium_temp = medium_temperature(temp_max, temp_min)
    med_temp.append(midium_temp)

print(f"La temperatura media de los {days} dias es: {midium_temp}°C.")

#ejercicio.6
from tp5_funciones import space_phrase

phrase = input("Ingrese una frase: ")
phrase_space = space_phrase(phrase)
print(phrase_space)


#ejercicio.7
from tp5_funciones import find_max_min

numbers = []
value_numbers = int(input("Ingrese la cantidad de numeros que desea comparar: "))

for i in range(value_numbers):
    value = float(input(f"Ingrese el valor {i+1}: "))
    numbers.append(value)

max, min = find_max_min(numbers)

if max is not None and min is not None:
    print(f"El valor maximo es {max}")
    print(f"El valor minimo es: {min}")
else: 
    print("No se ingreso ningun valor por lo que la lista esta vacia.")


#ejercicio.8
from tp5_funciones import area_perimetro

radio = float(input("Ingrese el radio de la circunferecncia: "))
area_perimetro(radio)

#ejercicio.9
from tp5_funciones import login
name = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")
login(name,password)

#ejercicio.10
from tp5_funciones import aply_discount
prices={2000:10, 4000:20, 6000:30}

print(f"El precio final de su carrito es de {aply_discount(prices)}")

#ejercicio.11
from tp5_funciones import aply_function,multiply_by_two
numbers=[2,6,10,43,84]

results=aply_function(multiply_by_two, numbers)

for i in range(len(numbers)):
    print(f"{numbers[i]} multiplicado por 2 es igual a {results[i]}")


#ejercicio.12
from tp5_funciones import separate_phrase

phrase=input("Ingrese una frase: ")
print(separate_phrase(phrase))

#ejercicio.13
from tp5_funciones import calculate_module
vector = (3, 4, 5)

module = calculate_module(vector)

print("El módulo del vector es:", module)

#Ejercicio 14
from tp5_funciones import is_prime

num=int(input("Ingrese un número: "))

if is_prime(num)==True:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")

#Ejercicio 15
from tp5_funciones import list_filler,factorial_calculator

nums=[]
list_filler(nums)

print("Factoriales de los números ingresados: ")
for num in nums:
    factorial=factorial_calculator(num)
    print(f"El factorial de {num} es {factorial}")

print(f"Se leyeron {len(nums)} números en total")

#Ejercicio 16
from tp5_funciones import frequency
num=int(input("Ingrese un número: "))
digit=int(input("Ingrese un digito: "))

print(f"El número {digit} se repite {frequency(num, digit)} veces en {num}")

#Ejercicio 17
from tp5_funciones import is_prime,sum_of_digit,frequency,factorial_calculator
max_num=0

while True:
    num=int(input("Ingrese un número primo: "))
    if is_prime(num):
       if num>max_num:
           max_num=num
       
       print(f"La suma de los dígitos de {num} es {sum_of_digit(num)}")
       digit=int(input("Ingrese un dígito: "))
       print(f"El número {digit} se repite {frequency(num, digit)} veces en {num}")
    else:
        break

factorial=factorial_calculator(max_num)
print(f"El mayor número ingresado fue {max_num}")
print(f"El factorial de {max_num} es {factorial}")
"""
