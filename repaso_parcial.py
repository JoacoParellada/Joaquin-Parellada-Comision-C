"""
#ejercicio.1

word=input("Ingresa una frase o palabra: ")

if len(word) == 4:
    word+="!"
else:
    word+="?"
print(word)

#ejercicio.2
#ejercicio.3

phrase = input("Ingresa una frase o cadena de texto: ")

words = phrase.split()
amount_words = len(words)

print(f"La frase ingresada contiene {amount_words} palabras.")

#ejercicio.4

month = input("S-Si asistio todo el mes\nN-No asistio todo el mes: ").lower()
hours = float(input("Ingrese la cantidad de horas que trabajo los dias domingo: "))
salary = float(input("Ingrese su salario: "))

if month == "s":
    if hours >= 6 and hours <= 10:
        additional = (salary*0.10)+salary
    elif hours >= 3 and hours <= 5:
        additional = (salary*0.03)+salary
    elif hours < 3:
        additional=salary
elif month == "n":
    if hours >= 3 and hours <=10:
        additional = (salary*0.02)+salary
    elif hours < 3:
        additional=salary

print(f"El monto final de su salario es ${additional}")

#ejercicio.5

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

if num1 == num2:
    result = num1 * num2
    print(f"{num1}x{num2}={result}")
elif num1 > num2: 
    result = num1 - num2
    print(f"{num1}-{num2}={result}")

elif num1 < num2:
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
"""
#ejercicio.6

age = int(input("Ingrese la edad de la persona:"))
antiquity = int(input("Ingrese los años de antiguedad en empleo: "))

if age > antiquity:
    if age >= 60 and antiquity < 25:
        print("La persona tiene jubilacion por edad.")
    elif age < 60  and antiquity >= 25:
        print("La persona tiene jubilacion por antiguedad joven.")
    elif age >= 60 and antiquity >= 25:
        print("La persona tiene una jubilacion por antiguedad adulta.")
elif age < 0 or antiquity < 0:
        print("[ERROR] Ingresa valores positivos.")
elif age < antiquity:
     print("[ERROR] Los datos ingresados no son correctos.")





