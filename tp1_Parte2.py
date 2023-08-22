#Trabajo práctico nro. 1 – Parte 2

#ejercicio.1

"""
base=float(input("Ingrese el valor de la base del rectangulo: "))
altura=float(input("Ingrese el valor de la altura del rectacgulo: "))

perimetro=2*(base+altura)
area=base*altura

print(f"El perimetro del rectangulo es: {perimetro}")
print(f"El area del rectangulo es: {area}")
"""

#ejercicio.2

"""
cat1=float(input("Ingrese el valor del primer cateto: "))
cat2=float(input("Ingrese el valor del segundo cateto: "))

hipotenusa=(cat1**2+cat2**2)**0.5 

print("El valor de la hipotenusa es de", hipotenusa)
"""
#ejercicio.3

"""
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))

suma=num1+num2
resta=num1-num2
division=num1/num2
multiplicacion=num1*num2

print("Suma=", suma)
print("Resta=", resta)
print("Division=", division)
print("Multiplicacion=", multiplicacion)
"""
#ejericicio.4

"""
fahrenheit=float(input("Ingrese valor de grados Fahrenheit: "))
celsius=(fahrenheit-32)*5/9
print(fahrenheit,"grados Fahrenheit son",celsius,"grados Celsius.")
"""
#ejercicio5

#a) El nombre de la variable esta en mayusculas, lo cual es una mala practica. 
#   La variable "nombre" no esta definida y esta dentro del input lo que hace que 
#   se produzca un error ya que solo se le puede pasar un solo argumento.
#    nombre= input("¿Cuál es tu canción favorita?")

#b) En la primera linea no se esta especificando el tipo de dato que se quiere ingresar
#   por lo tanto el programa lo toma como un str y en la segunda linea salta el error ya
#   que no se pueden hacer operaciones matematicas con un str.
#   precio = float(input("Precio: "))
#   total = precio + (precio * 0.1)

#c) En la segunda linea faltan comillas al texto de salida dentro del print.
#   edad = int(input("Edad: "))
#   print("tu edad es", edad)

#d) Interpretando que el programa quiere verificar si la edad ingresada es 18 falta 
#   agregar la expresion booleana "==" para que se imprima el mensaje "true/false"
#   edad = int(input("Edad: "))
#   print("Veamos si tu edad es 18…", edad==18)

#ejercicio.6
"""
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
promedio=(num1+num2+num3)/3
print("El promedio de los numeros ingresados es:",promedio)
"""
#ejercicio.7
"""
min=int(input("Ingrese una cantidad de minutos: "))
hs=min//60
min_restantes=min%60
print(f"{min} minutos son {hs} horas y {min_restantes} minutos.")
"""
#ejercicio.8
"""
sueldo_base=float(input("Ingrese su sueldo: "))
venta1=float(input("Ingrese el valor de la primer venta: "))
venta2=float(input("Ingrese el valor de la segunda venta: "))
venta3=float(input("Ingrese el valor de la tercer venta: "))
comision=(venta1+venta2+venta3)*0.10
sueldo_total=sueldo_base+comision
print(f"El sueldo total es de ${sueldo_total}")
"""
#ejercicio.9
"""
precio_compra=float(input("Ingrese el valor de su compra: "))
descuento=precio_compra*0.15
precio_final=precio_compra-descuento
print("El precio final de su compra es de $",precio_final)
"""
#ejercicio.10
"""
parcial1=float(input("Ingrese calificacion del primer parcial: "))
parcial2=float(input("Ingrese calificacion del segundo parcial: "))
parcial3=float(input("Ingrese calificacion del tercer parcial: "))
promedio_parciiales=(parcial1+parcial2+parcial3)/3
porcentaje_parciales=promedio_parciiales*0.55

examen_final=float(input("Ingrese calificacion del examen final: "))
porcentaje_examen_final=examen_final*0.30

trabajo_final=float(input("Ingrese calificacion del trabajo final: "))
porcentaje_trabajo_final=trabajo_final*0.15

nota_final=(porcentaje_examen_final+porcentaje_parciales+porcentaje_trabajo_final)
print(f"La calificacion final de la materia Algoritmos es: {nota_final:.2f}")
"""
#ejericicio.11
"""
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
distancia=abs(num1-num2)
print(f"La distancia entre los numeros ingresados es {distancia:.2f}")
"""
#ejercicio.12
"""
num=float(input("Ingrese un numero: "))
raiz_cuadrada= num**0.5
raiz_cubica= num**(1/3)
print(f"La raiza cuadrada de {num} es :{raiz_cuadrada}")
print(f"La raiza cubica de {num} es :{raiz_cubica}")
"""
#ejercicio.13
"""
num = int(input("Ingrese un número de dos cifras: "))
dig1=num//10
dig2=num%10
invertido=dig2*10+dig1
print(f"El numero invertido es: {invertido}")
"""
#ejercicio.14
"""
a=float(input("Ingrese el valor A:"))
b=float(input("Ingrese el valor B:"))
aux=a
a=b
b=aux
print("La variable A ahora es: ",a)
print("La variable B ahora es: ",b)
"""
#ejercicio.15

#No entendi el ejercicio

#ejercicio.16
"""
nombre=input("Ingrese su nombre: ")
apellido1=input("Ingrese su primer apellido: ")
apellido2=input("Ingrese su segundo apellido: ")
inicial_nombre=nombre[0]
inicial_apellido1=apellido1[0]
inicial_apellido2=apellido2[0]
print("La incial de tu nombre ",inicial_nombre.upper())
print("La incial de tu primer apellido ",inicial_apellido1.upper())
print("La incial de tu nombre ",inicial_apellido2.upper())
"""
#ejercicio.17
"""
usuario=input("Ingrese su nombre de usuario: ")
print("Ahora estas en la matrix",usuario)
"""
#ejercicio.18
"""
costo=float(input("Ingrese el costo de la cena: "))
servicio=costo*0.062
propina=costo*0.10
costo_final=costo+servicio+propina
print(f"El costo final de la cena es de $ {costo_final:.2f}")
"""
#ejercicio.19
"""
anio=int(input("Ingresa el año de tu nacimiento: "))
mes=int(input("Ingresa el mes de tu nacimiento: "))
dia=int(input("Ingresa el dia de tu nacimiento: "))
fecha_nacimiento=f"{dia}/{mes}/{anio}"
print("La fecha de nacimiento es: ",fecha_nacimiento)
"""
#ejercicio.20
"""
fecha_nacimiento=input("Ingresa tu fecha de nacimiento (DDMMAAAA): ")
dia=int(fecha_nacimiento[:2])
mes=int(fecha_nacimiento[2:4])
anio=int(fecha_nacimiento[4:])
print(f"Tu fecha de nacimiento es: {dia}/{mes}/{anio}")
"""
#ejercicio.21
"""
km_litro=float(input("Ingrese cantidad de km que puede recorrer con 1L de combustible: "))
capacidad_tanque=float(input("Ingrese la capacidad del tanque de combustible en litros: "))
km_recorrido=float(input("Ingrese la cantidad de km que desea recorrer: "))
litros=km_recorrido/km_litro
tanques=litros/capacidad_tanque
print(f"Se necesitan {tanques} tanques de combustible para recorrer los {km_recorrido} kilometros.")
"""