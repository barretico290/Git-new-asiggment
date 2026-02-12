def Calculadora ():
    print("=== Calculadora ===")
    print("1. sumar")
    print("2. restar")

    opcion = input("Elige una opción (1-2): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif opcion == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)
