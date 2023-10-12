import math
#ejercicio.1
def validation_dni(dni):
    if len(dni) < 7  or len(dni) > 8:
        print("El DNI ingresado no es valido.")
        return False
    else:
        print("El DNI ingresado es valido ",dni)
        return True
#ejercicio.2
def long_last_word(phrase):
    phrase = phrase.strip()
    words = phrase.split()
    if words:
        last_word = words [-1]
        return len(last_word)
    else:
        return 0 

#ejercicio.3
def generate_id(dni,name1,name2,last_name):
    name = ""
    while len(name) == 0:
        name = input("Ingrese su nombre completo: ")
        dni = input("Ingrese su DNI: ")
        name1 = name.split(" ")[0]
        name2 = name.split(" ")[1]
        last_name = name.split(" ")[2]
        id = name1 + str(len(last_name)) + dni[:3]
        return id
    
#ejercicio.4
def is_multiple(n1,n2):
    if n2 == 0:
        return False
    return n1 % n2 == 0

#ejercicicio.5

def medium_temperature(temp_max,temp_min):
    return (temp_max + temp_min) / 2

#ejercicio.6

def space_phrase(phrase):
    phrase_space = " ".join(phrase)
    return phrase_space

#ejercicio.7

def find_max_min(list):
    if not list:
        return None, None
    
    max = min = list[0]

    for value in list:
        if value > max:
            max = value
        elif value < min:
            min = value
            
    return max, min
#ejercicio.8
pi = math.pi

def area_perimetro(radio):
    area = pi * (radio ** 2)
    perimetro = 2 * pi * radio
    return print(f"El area de la circunferencia es de: {area}\nEl perimetro de la circunferencia es de: {perimetro}")

#ejercicio.9
trys = 0

def login(name,password):
    global trys
    while trys != 2:
        if name == "usuario1" and password == "asdasd":
            return print(f"Usuario y contraseña correctos.Bienvenido {name}")
        else:
            trys += 1
            print("El usuario o la contraseña ingresada son incorrectos.")
            name = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
    print("Agotaste los intentos... vuelve mas tarde.")
            
#ejercicio.10

def aply_discount(prices):
    final_price=0
    shopping_cart=float(input("Ingrese el monto total de su carrito de compra: "))
    if shopping_cart<=0:
        print("¡ERROR! El valor ingresado no es válido")
        aply_discount(prices)
    else:    
        if shopping_cart>=2000 and shopping_cart<4000:
            discount=(shopping_cart*prices[2000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[2000]}%")

        elif shopping_cart>=4000 and shopping_cart<6000:
            discount=(shopping_cart*prices[4000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[4000]}%")

        elif shopping_cart>=6000:
            discount=(shopping_cart*prices[6000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[6000]}%")

        else:
            final_price=shopping_cart
            print(f"Por el monto de su carrito no obtiene ningún descuento")

        return final_price

#ejercicio.11

def aply_function(func, numbers):
    results=[]
    
    for num in numbers:
        results.append(func(num))
    
    return results
def multiply_by_two(num):
    
    return num*2

#ejercicio.12

def separate_phrase(phrase):
    words={}
    key=1
    
    for element in phrase.split():
        words[key]=element
        key+=1
    return words

#ejercicio.13

def calculate_module(vector):
    x, y, z = vector
    module = math.sqrt(x**2 + y**2 + z**2)
    return module

#Ejercicio 14
def is_prime(num):
    counter=0
    for i in range(1,num+1):
        if num%i==0:
            counter+=1
    
    if counter==2:
        return True
    else:
        return False

#Ejercicio 15
def list_filler(nums):
    num=1
    while num!=0:
        num=int(input("Ingrese un número, para dejar de ingresar números ingrese 0(cero): "))
        if num!=0:
            nums.append(num)
    return nums

def factorial_calculator(num):
    if num==0:
        return 1
    else:
        return num*factorial_calculator(num-1)

#Ejercicio 16
def frequency(num, digit):
    num_str=str(num)
    digit_str=str(digit)
    counter=0

    for i in num_str:
        if i==digit_str:
            counter+=1
    return counter

#Ejercicio 17
def sum_of_digit(num):
        digits_sum=0
        num_str=str(num)
        for i in num_str:
            digits_sum+=int(i)
        return digits_sum






