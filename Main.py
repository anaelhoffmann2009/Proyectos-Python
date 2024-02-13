# Password Generator in Python

import random

caracteres = "$#?*%ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"

def createPassword():
    ask = int(input("¿Cuántos carácteres quiere que tenga su contraseña?: "))
    password = ""

    for i in range(ask):
        x = random.choice(caracteres)
        password += x

    print(f"Su contraseña creada es: {password}")

createPassword()