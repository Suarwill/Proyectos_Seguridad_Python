import random
import string

def generar_texto_aleatorio(longitud):
    caracteres = string.ascii_letters + string.digits
    texto = ''.join(random.choice(caracteres) for _ in range(longitud))
    return texto

def crear_archivo_aleatorio(texto):
    nombre_archivo = ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + ''
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)
    print(f"Archivo creado: {nombre_archivo}")

cantidad = int(input("ingrese cantidad de archivos random a realizar: "))

for i in range (0,cantidad):
    # Crear el archivo con el nombre aleatorio
    longitud = random.randint(1084000,3200048)
    texto_aleatorio = generar_texto_aleatorio(longitud)

    crear_archivo_aleatorio(texto_aleatorio)