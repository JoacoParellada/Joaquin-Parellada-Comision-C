#ejercicio.1
"""
word=input("Ingrese una palabra: ")
for i in range(10):
    print(word)
"""
#ejercicio.2
"""
age=int(input("Ingrese su edad: "))
for (i) in range(age):
    print(i+1)    
"""
#ejercicio.3
"""
num=int(input("Ingrese un numero: "))

impares=[]
for i in range(num):
    if i % 2 == 0:
        impares.append(str(i+1))

impares_separados = ", ".join(impares)
print("Numeros impares: ",impares_separados)
"""
#ejercicio.4
"""
num=int(input("Ingrese un numero: "))
count= []
for i in range(num,-1,-1):
    count.append(str(i))

countdown=", ".join(count)
print(f"La cuenta regresiva es: {countdown}")
"""
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
"""
num=int(input("Ingrese un numero: "))

for i in range(num+1):
    print("*"*i)
"""
#ejercicio.7
"""
for i in range(1,11):
    print("----------------")
    print("La tabla del: ",i)
    for f in range(1,11):
        print(i,"x",f,"=",i*f)
"""
#ejercicio.8