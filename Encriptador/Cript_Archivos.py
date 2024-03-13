from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def leerClave():    # La clave debe ser de 16, 24 o 32 bytes según el modo AES a usar
    with open('key.txt', 'rb') as file:
        key = file.read()
    return key

def leerIV():       # Vector de inicialización (16 bytes)
    with open('IV.txt', 'rb') as file:
        iv = file.read()
    return iv

def encriptar(key,iv):
    archivo = str(input("nombre del archivo a encriptar: "))     # Contenido a Encriptar
    with open(archivo, 'rb') as file:
        data = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    archivoEncriptado = archivo[:-4] + '.enc'        # Nombre del archivo encriptado

    with open(archivoEncriptado, 'wb') as archivoEncriptado:
        encrypted_data = cipher.encrypt(padded_data)
        archivoEncriptado.write(encrypted_data)
    
    print("Datos cifrados en: ", archivoEncriptado)

    return archivoEncriptado

def desencriptar(key, iv):
    archivo_encriptado = input("Nombre del archivo a desencriptar: ")

    with open(archivo_encriptado, 'rb') as file:
        encrypted_data = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Eliminar el relleno manualmente
    unpadded_data = decrypted_data[:-decrypted_data[-1]]

    archivo_desencriptado = archivo_encriptado[:-4] + '_desencriptado.txt'  # Eliminar la extensión ".enc"

    with open(archivo_desencriptado, 'wb') as file:
        file.write(unpadded_data)

    print("Datos desencriptados en:", archivo_desencriptado)
    return archivo_desencriptado

def __init__():
    key = leerClave()  
    iv = leerIV()
    while (True):
        print("Este es un archivo para encriptar y desencriptar archivos. \n \n")
        Opcion = input("Que desea realizar. \n(e)ncriptar o (d)esencriptar:")
        
        if Opcion == "e":
            encriptar(key,iv)
            print("\n"*5)
        elif Opcion == "d":
            desencriptar(key, iv)
            print("\n"*5)
        else:
            print("Elija una opcion correcta")
            print("\n"*5)


__Init__ = __init__()