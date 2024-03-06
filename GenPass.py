# Generador de contraseñas aleatorias.
import string
import random

longitudContraseña = int(input("Ingrese el largo de la contraseña aleatoria: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for i in range(longitudContraseña))

print("La contraseña aleatoria es: " + contraseña)