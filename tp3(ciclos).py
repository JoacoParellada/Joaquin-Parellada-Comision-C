#ejercicio.1
"""
word=input("Ingrese una palabra: ")

for i in range(10):
    print(word)

#ejercicio.2

age=int(input("Ingrese su edad: "))

if age > 0:
    for i in range(age):
        print(f"Cumpliste {i+1} años!")
else: 
    print("[ERROR] Ingrese un valor positivo.")

#ejercicio.3

num=int(input("Ingrese un numero: "))
odd=[]

if num > 0:
    for i in range(num+1):
        if i % 2 == 1:
            odd.append(str(i))
    print(", ".join(odd))
else:
    print("[ERROR] Ingrese un valor positivo.")

#ejercicio.4

num=int(input("Ingrese un numero: "))
account=[]
if num > 0:
    for i in reversed(range(num+1)):
        account.append(str(i))
    print(", ".join(account))
else:
    print("[ERROR] Ingrese un valor positivo.")


#ejercicio.5

investment_amount=float(input("Ingrese la cantidad a invertir: "))
interest=float(input("Ingrese el porcentaje de interes anual: "))
years=int(input("Ingrese la duracion de la inversion en años: "))

for i in range(years):
    profit=((investment_amount*interest)/100)*(i+1)
    profit_for_year=profit+investment_amount
    profit_total=(profit+profit_for_year)*years
    print(f"La ganancia obtenida en el año {i+1} es de ${profit} y la ganancia total es de ${profit_for_year} ")
print(f"La ganancia de la inversion en los {years} años es de ${profit_total}")

#ejercicio.6

num=int(input("Ingrese un numero: "))
if num > 0:
    for i in range(num+1):
        print("*"*i)
else:
    print("[ERROR] Ingrese un valor positivo.")

#ejercicio.7

for i in range(1,11):
    print(f"---TABLA DEL {i}---")
    for j in range(1,11):
        product=i*j
        print(f"{i}x{j}={product}")

#ejercicio.8

num=int(input("Ingrese un número entero: "))
value=1

for i in range(1, num+1):
    row_value=value

    for j in range(i):
        print(row_value,end=" ")
        row_value-=2

    print()
    value+=2


#ejercicio.9

password=""

while password != "contraseña":
    password=input("Ingrese la contraseña: ")
    if password != "contraseña":
        print("Contraseña incorrecta, intente nuevamente.")

print("Contraseña correcta.")

#ejercicio.10

num=int(input("Ingrese un número entero: "))
counter=0

for i in range(num):
    if num%(i+1)==0:
        counter=counter+1
if counter==2:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
    
#ejercicio.11

word=input("Ingrese una palabra: ")
for i in reversed(word):
    print(i)


#ejercicio.12

phrase=input("Ingrese una frase: ")
character=input("Ingrese una letra: ")

counter=0

for i in range(len(phrase)):
    if character == phrase[i]:
        counter += 1

print(f"La letra {character} aparece {counter} veces en la frase: {phrase}")

#ejercicio.13

word=""
while word != "salir":
    word=input("Ingrese una palabra: ")
    if word != "salir":
        print(word)
    else:
        print("saliendo...")

#ejercicio.14

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

pair=[]
odd=[]
if num2 > num1:
    for i in range(num1,num2+1):
        if i % 2 == 0:
            pair+=[i]
        else:
            odd+=[i]
    print(f"Los numeros pares desde el {num1} hasta {num2} son {pair}\nY los numeros impares desde el {num1} hasta {num2} son {odd}.")
else:
    for i in range(num2,num1+1):
        if i % 2 == 0:
            pair+=[i]
        else:
            odd+=[i]
    print(f"Los numeros pares desde el {num2} hasta {num1} son {pair}\nY los numeros impares desde el {num1} hasta {num2} son {odd}.")

#ejercicio.15

num=int(input("Ingrese un numero para averiguar sus divisores: "))
dividers=[]
if num > 0:
    for i in range(1,num+1):
        if num % i == 0:
            dividers.append(i)
    print(f"Los divisores del numero {num} son: {dividers}")
else:
    print("[ERROR] El valor ingresado debe ser mayor a 0.")


#ejercicio.16

amount_numbers=int(input("Ingrese la cantidad de numeros para ingresar: "))
negative=0
for i in range(amount_numbers):
    num=float(input(f"Ingresa el numero {i+1}: "))
    if num < 0:
        negative=negative+1
        
print(f"La cantidad de numeros negativos ingresados es: {negative}")

#ejercicio.17
phrase = input("Ingrese una frase: ")
phrase = phrase.lower()

vowels=[]

for letra in phrase:
    if letra in "aeiuo" and letra not in vowels:
        vowels.append(letra)
print(vowels)

#ejercicio.18

fibo=[0,1]

for i in range(2,10):
    next_num=fibo[i-1]+fibo[i-2]
    fibo.append(next_num)

for num in fibo:
    print(num)
#ejercicio.19

amount=float(input("Ingrese la cantidad que desea ahorrar: $"))

if amount<0:
    print("[ERROR] Ingrese un valor positivo")
else:
    saving=0

    while saving<=amount:
        new_saving=float(input("Ingrese el monto que desea ingresar: $"))

        if new_saving<0:
            print("[ERROR] Ingrese un valor positivo")
        else:
            saving+=new_saving
            remaining=amount-saving
    
        if saving >= amount:
            print(f"Felicitaciones consiguio el objetivo!")
            print(f"Objetivo: ${amount}\nAhorros totales: ${saving}")

#ejercicio.20

num=1
addition=0
while num != 0:
    num=int(input("Ingrese un numero: "))

    print("Para salir ingrese 0.")
    if num<0:
        print("[ERROR] Ingrese valores positivos")
    else:
        addition=addition+num
print(f"La suma de los numero ingresados es: {addition}")

#ejercicio.21

num=1
major=0
while num != 0:
    num=int(input("Ingrese un numero: "))

    print("Para salir ingrese 0.")
    if num < 0:
        print("[ERROR] Ingrese valores positivos")
    elif num > major:
        major=num
        
print(f"El mayor de los numero ingresados es: {major}")

#ejercicio.22

num=0
addition=0
pair=0

while num!= -1:
    num=int(input("Ingrese un numero positivo: "))
    if num < -1:
        print("[ERROR] Ingrese solo numeros positivos.")
    elif(num!=-1):
        addition+=num
        print(f"La suma es: {addition}")
        if num % 2 == 0:
            pair+=1
print(f"Se ingresaron {pair} numeros pares")

#ejercicio.23

num=1
total_amount=0

while num!= 0:
    num=int(input("Ingrese el monto de las compras: "))
    if num < 0:
        print("[ERROR] Ingrese solo numeros positivos.")
    elif(num!=0):
        total_amount+=num
print(f"El monto total de la compra es: ${total_amount}")
#ejercicio.24

num=1
total_amount=0

while num!= 0:
    num=int(input("Ingrese el monto de las compras: "))
    if num < 0:
        print("[ERROR] Ingrese solo numeros positivos.")
    elif(num!=0):
        total_amount+=num

if total_amount > 1000:
    print("Obtuviste un descuento de 10% en tu compra!")
    discount=(total_amount*0.10)
    total_amount=total_amount-discount

print(f"El monto total de la compra es: ${total_amount}")


#ejercicio.25

num=int(input("Ingrese un numero positivo: "))

if num<0:
    print("[ERROR]El valor ingresado es negativo.")
elif num==0:
    print("El factorial de 0 es 1")
else:
    factorial=1

    for i in range(1, num+1):
        factorial*=i

    print(f"El factorial de {num} es {factorial}")
"""

    





