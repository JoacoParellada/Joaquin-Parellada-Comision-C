"""
#ejercicio.1
x = 0

while x <= 30:
    x += 1
    if x == 15:
        print(f"Se rompio la ejecucion del bucle cuando x valia: {x}")
        break
    if x in [4,6,10]:
        print(f"Se salto el valor {x} de x")
        continue
    print(x)

#ejercicio.2

print("Ingrese lineas y ingrese un espacio para finalizar.")

lines = []

while True:
    line = input("> ").strip()
    if line == "":
        break
    lines.append(line)
    
for i in lines:
    print(i.upper())

#ejercicio.3

balance = 0
print("Ingrese bitacora de operaciones, ingrese linea en blanco para finalizar.")
print("D- Para depositar.\nR- Para retirar.")

while True:
    operation = input("> ").upper().strip()
    if operation == "":
        break
    oper= operation.split()
    if len(oper) != 2:
        print("[ERROR] La cantidad de valores ingresados no es correcta.")
        continue
    c = oper[0]
    a = int(oper[1])

    if c == "D":
        balance += a
    elif c == "R":
        balance -= a
    else:
        print("[ERROR] La opcion ingresada no es correcta.")


print(f"El saldo acutal de la cuenta es es: ${balance}")

#ejercicio.4
numero = int(input('Digite un numero primo recuerde que un numero primo es aquel que solo se divide entre el mismo y el 1, digite cero para terminar:'))
numeros_primos = []
primo = True

while numero != 0:
    if numero == 1:
        print('Nota: Recuerda que un numero primo es mayor a 1')
        continue
    for i in range(2,numero):

        if numero%i==0 and i!=1 and i!=numero:
            primo = False
            break
        else: 
            primo= True
    if primo==True:
        numeros_primos.append(numero)
    numero = int(input('Digite un numero primo recuerde que un numero primo es aquel que solo se divide entre el mismo y el 1:'))
else:
    print(f'El numero de total de primos ingresados es de {len(numeros_primos)}')

#ejercicio.5
age1 = input('Ingrese un primer año: ')
age2 = input('Ingrese el siguiente año: ')
for i in range(age1,age2+1):

    if i%4==0 and i%10==0 and not i%100==0:
        print(i)
    elif i%400==0:
        print(i)
    else:
        continue

#ejercicio.6
for i in range(1,21):
       if i%2==0:
               print(i)
       else:
           continue

#Ejercicio 7
numbers=[7,8,1,9]
num=int(input("Ingrese un número para saber si se encuentra en la lista: "))

for i in numbers:
   if num==i:
       print(f"El número {num} si se encuentra en la lista")
       break
   else:
       continue
"""

#Ejercicio 8
print(f"¡BIENVENIDO! A continuación verá las diferentes opciones de menú\n1- Milanesa con puré\n2- Tarta de jamón y queso\n3- Ñoquis con tuco\n0- Salir")
option=1
account=0
count=[]
while option!=0:
   option=int(input("Ingrese una opción: "))
   if option==0:
       break
   elif option==1:
       print("Milanesas con pure: $1200")
       account+=1200
       count.append(1)
   elif option==2:
       print("Tarta de jamón y queso: $1400")
       account+=1400
       count.append(2)
   elif option==3:
       print("Ñoquis con tuco: $1500")
       account+=1500
       count.append(3)
   else:
       print("¡ERROR! Ingrese una opción válida")
print(f"Usted ha pedido los siguientes menús: {count}\nLa cuenta total es de ${account}")


