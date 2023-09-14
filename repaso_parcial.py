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
"""

month = input("S-Si asistio todo el mes\nN-No asistio todo el mes)").lower()
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









