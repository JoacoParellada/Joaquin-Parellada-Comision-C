print('Ingrese la fecha con el formato solicitado:')
fecha_input = input('Formato: [Día de la semana], [DD/MM]: ')

parts = fecha_input.split(",")
dia_semana = parts[0].lower()
dia, mes = map(int, parts[1].split('/'))
dias_validos = ("lunes","martes","miercoles","jueves","viernes")

if dia_semana in dias_validos:
    if dia < 1  or dia > 31:
        print(f"[ERROR:] El dia ingresado no es valida ")
        quit()
    elif mes < 1 or mes > 12:
        print("[ERROR:] El mes ingresado no es valida")
        quit()
    elif dia > 28 and mes == 2:
        print("[ERROR:] El mes Febrero contiene 28 dias")
        quit()
    elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        print("[ERROR:] El mes ingresado no contiene mas de 30 dias")
        quit()
else:
    print("[ERROR:] El dia de la semana ingresado no es valido")
    quit()

print("Día de la semana:", dia_semana)  
print("Día:", dia)
print("Mes:", mes)



if dia_semana == "jueves" or dia_semana == "viernes":
    opcion=2
else:
    print(f"¿El dia ({dia}/{mes}) se tomaron examenes?")
    opcion=int(input("Si=1\nNo=2: "))

if opcion == 1:
    if dia_semana == "lunes":
        print("Se tomo examen al nivel inicial")
        cant_desaprobados=int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
        cant_aprobados=int(input("Ingrese la cantidad de alumnos aprobados: "))
        porcentaje_aprobados=cant_aprobados/(cant_desaprobados+cant_aprobados)
        print(f"El porcentaje de alumnos aprobados es de : %{(porcentaje_aprobados*100)}")
    if dia_semana == "martes":
        print("Se tomo examen al nivel intermedio")
        cant_desaprobados=int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
        cant_aprobados=int(input("Ingrese la cantidad de alumnos aprobados: "))
        porcentaje_aprobados=cant_aprobados/(cant_desaprobados+cant_aprobados)
        print(f"El porcentaje de alumnos aprobados es de : %{(porcentaje_aprobados*100)}")
    if dia_semana == "miercoles":
        print("Se tomo examen al nivel avanzado")
        cant_desaprobados=int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
        cant_aprobados=int(input("Ingrese la cantidad de alumnos aprobados: "))
        porcentaje_aprobados=cant_aprobados/(cant_desaprobados+cant_aprobados)
        print(f"El porcentaje de alumnos aprobados es de : %{(porcentaje_aprobados*100)}")
elif opcion ==2:
    if dia_semana == "jueves":
        print("Los dia jueves corresponden a las clases de practica hablada")
        porcentaje_asistencia=int(input("Ingrese el porcentaje de alumnos que asistio a la clase: "))
        if porcentaje_asistencia < 1 or porcentaje_asistencia > 100:
            print("El porcentaje ingresado es invalido")
        elif porcentaje_asistencia > 50:
            print("Asistio la mayoria de los alumnos")
        else:
            print("No asistio la mayoria de los alumnos")
    elif dia_semana == "viernes":
        if (dia == 1 and mes == 1) or (dia == 1 and mes == 7):
            print("Comienzo de nuevo ciclo")
            cant_alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: ")) 
            arancel=int(input("Ingrese valor del arancel por alumno: "))
            print(f"El ingreso total del nuevo ciclo es de: ${(cant_alumnos*arancel)}")
    else:
        print("No hay informacion para proporcionar.")
else:
    print("[ERROR] La opcion ingresada no es correcta")