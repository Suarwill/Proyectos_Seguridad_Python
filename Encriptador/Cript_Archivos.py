# ============================ Librerías ============================
import importlib
import subprocess
import sys
import platform
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def libSetup(*libs):
    """Instala automáticamente las librerías necesarias si no están disponibles."""
    for entry in libs:
        if isinstance(entry, tuple):
            lib, apt_pkg = entry
        else:
            lib, apt_pkg = entry, None
        try:
            importlib.import_module(lib)
        except ImportError:
            if platform.system() == 'Linux':
                print(f"[+] Instalando {lib} con APT...")
                pkg = apt_pkg or lib
                subprocess.check_call(['sudo', 'apt', 'install', '-y', pkg])
            else:
                print(f"[+] Instalando {lib} con pip...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])

# Configurar librerías necesarias
libSetup(('pycryptodome', 'python3-pycryptodome'))

# ============================ Funciones ============================
def leer_clave():
    """Lee la clave AES desde un archivo."""
    with open('key.txt', 'rb') as file:
        return file.read()

def leer_iv():
    """Lee el vector de inicialización (IV) desde un archivo."""
    with open('IV.txt', 'rb') as file:
        return file.read()

def encriptar(key, iv):
    """Encripta un archivo usando AES en modo CBC."""
    archivo = input("Nombre del archivo a encriptar: ").strip()
    try:
        with open(archivo, 'rb') as file:
            data = file.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data, AES.block_size)
        archivo_encriptado = archivo.rsplit('.', 1)[0] + '.enc'

        with open(archivo_encriptado, 'wb') as file:
            file.write(cipher.encrypt(padded_data))

        print(f"Datos cifrados en: {archivo_encriptado}")
        return archivo_encriptado
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor, verifique el nombre del archivo.")

def desencriptar(key, iv):
    """Desencripta un archivo previamente cifrado con AES en modo CBC."""
    archivo_encriptado = input("Nombre del archivo a desencriptar: ").strip()
    try:
        with open(archivo_encriptado, 'rb') as file:
            encrypted_data = file.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data)
        unpadded_data = unpad(decrypted_data, AES.block_size)

        archivo_desencriptado = archivo_encriptado.rsplit('.', 1)[0] + '_desencriptado.txt'

        with open(archivo_desencriptado, 'wb') as file:
            file.write(unpadded_data)

        print(f"Datos desencriptados en: {archivo_desencriptado}")
        return archivo_desencriptado
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor, verifique el nombre del archivo.")
    except ValueError:
        print("Error al desencriptar. Verifique que la clave y el archivo sean correctos.")

# ============================ Main ============================
def main():
    """Función principal para ejecutar el script."""
    key = leer_clave()
    iv = leer_iv()

    print("Este es un script para encriptar y desencriptar archivos.\n")
    while True:
        opcion = input("¿Qué desea realizar? (e)ncriptar, (d)esencriptar o (s)alir: ").strip().lower()
        if opcion == 'e':
            encriptar(key, iv)
        elif opcion == 'd':
            desencriptar(key, iv)
        elif opcion == 's':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción correcta.")

if __name__ == "__main__":
    main()