from funciones_calcu import *
from os import system

def mostrar_menu(a, b):
    print("\nMenú:")
    print("1. Sumar A y B")
    print("2. Restar A y B")
    print("3. Dividir A entre B")
    print("4. Multiplicar A y B")
    print("5. Calcular factorial de A y B")
    print("6. Ingresar otros números")
    print("7. Salir")

# Pedir al usuario que ingrese los operandos
a = float(input("Ingrese el primer operando (A): "))
b = float(input("Ingrese el segundo operando (B): "))

while True:
    mostrar_menu(a, b)
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        print("El resultado de A+B es:", suma(a, b))
    elif opcion == '2':
        print("El resultado de A-B es:", resta(a, b))
    elif opcion == '3':
        if b == 0:
            print("Error: No se puede dividir por cero.")
        else:
            print("El resultado de A/B es:", division(a, b))
    elif opcion == '4':
        print("El resultado de A*B es:", multiplicacion(a, b))
    elif opcion == '5':
        print("El factorial de A es:", factorial(int(a)), "y el factorial de B es:", factorial(int(b)))
    elif opcion == '6':
        a = float(input("Ingrese el primer operando (A): "))
        b = float(input("Ingrese el segundo operando (B): "))
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
