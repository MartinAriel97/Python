#Ejercicio sencillo de algoritmos
import random 

def jugar():
    print("ADIVINAR NÚMEROS ALEATORIOS DEL 1 AL 100")
    print("INGRESÁ NÚMEROS para ver si adivinás o no el número..")
    print("TENÉS 3 INTENTOS DISPONIBLES")

    # Generamos un número aleatorio del 1 al 100
    numero_secreto = random.randint(1, 100)
    numero_secreto = 50
    # Para probar podés dejarlo fijo:
    # numero_secreto = 50

    intentos = 0
    intentos_max = 3

    while intentos < intentos_max:
        numero_usuario = int(input("Ingrese un número del 1 al 100: "))

        if numero_usuario == numero_secreto:
            print("¡Acertaste el número secreto! GANASTE. El número secreto era:", numero_secreto)
            break
        elif numero_usuario < numero_secreto:
            print("Número demasiado bajo. Volvé a intentarlo.")
        else:
            print("Número demasiado alto. Volvé a intentarlo.")

        intentos += 1  # Aumenta la cantidad de intentos después de fallar

        if intentos < intentos_max:
            print(f"Te quedan {intentos_max - intentos} intentos.\n")
        else:
            print("\nSe te terminaron los intentos.")
            print(f"El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jugar()