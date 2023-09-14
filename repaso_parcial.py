"""
#ejercicio.1

word=input("Ingresa una frase o palabra: ")

if len(word) == 4:
    word+="!"
else:
    word+="?"
print(word)
"""
#ejercicio.2
import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "juego", "computadora", "teclado", "pantalla"]

# Elegir una palabra al azar
palabra = random.choice(palabras)

# Inicializar variables
intentos = 6  # Número de intentos permitidos
letras_adivinadas = []  # Lista para almacenar letras adivinadas

# Mostrar un mensaje de bienvenida
print("¡Bienvenido al juego de adivinar la palabra!")
print("Tienes", intentos, "intentos para adivinar la palabra.")

# Crear una cadena con guiones bajos para representar las letras no adivinadas
palabra_oculta = "_" * len(palabra)

# Bucle principal del juego
while intentos > 0:
    # Mostrar la palabra oculta
    print("Palabra:", palabra_oculta)
    
    # Solicitar una letra al usuario
    letra = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya se adivinó
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra. Intenta con otra.")
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    letras_adivinadas.append(letra)
    
    # Verificar si la letra está en la palabra
    if letra in palabra:
        print("¡Correcto! La letra está en la palabra.")
        # Actualizar la cadena de la palabra oculta con la letra adivinada
        palabra_oculta = "".join([letra if letra == p else oculta for p, oculta in zip(palabra, palabra_oculta)])
    else:
        print("Incorrecto. Esa letra no está en la palabra.")
        intentos -= 1
    
    # Verificar si el usuario adivinó toda la palabra
    if palabra_oculta == palabra:
        print("¡Felicidades! Adivinaste la palabra:", palabra)
        break

# Si el usuario se queda sin intentos, mostrar la palabra correcta
if intentos == 0:
    print("¡Perdiste! La palabra correcta era:", palabra)













