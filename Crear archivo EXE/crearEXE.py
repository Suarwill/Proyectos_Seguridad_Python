import subprocess
import os
import time
import shutil

PYTHON_VERSION = "python3.11"  # usa explícitamente python3.11

# Verificar si pyinstaller está instalado para python3.11
def instalar_pyinstaller():
    print("[+] Verificando si PyInstaller está instalado para Python 3.11...")
    try:
        subprocess.run([PYTHON_VERSION, "-m", "pyinstaller", "--version"], check=True, stdout=subprocess.DEVNULL)
        print("[✓] PyInstaller ya está instalado.")
    except subprocess.CalledProcessError:
        print("[+] PyInstaller no encontrado. Instalando para Python 3.11...")
        subprocess.run([PYTHON_VERSION, "-m", "pip", "install", "--user", "pyinstaller"], check=True)

# Crear el ejecutable
def crear_ejecutable():
    script_path = os.path.join("base", "main.py")
    if not os.path.isfile(script_path):
        print(f"[X] No se encontró el archivo {script_path}")
        exit(1)

    print(f"[+] Creando ejecutable desde {script_path} ...")
    subprocess.run([PYTHON_VERSION, "-m", "PyInstaller", "--onefile", script_path], check=True)

# Limpiar archivos y carpetas innecesarias
def limpiar_directorio():
    archivos_eliminar = ["main.spec"]
    carpetas_eliminar = ["build", "__pycache__"]

    for archivo in archivos_eliminar:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"[−] Archivo eliminado: {archivo}")

    for carpeta in carpetas_eliminar:
        if os.path.exists(carpeta):
            shutil.rmtree(carpeta)
            print(f"[−] Carpeta eliminada: {carpeta}")

    # Mantener solo dist y base
    for nombre in os.listdir():
        if nombre not in ["dist", "base", os.path.basename(__file__)]:
            if os.path.isfile(nombre):
                os.remove(nombre)
                print(f"[−] Archivo eliminado: {nombre}")
            elif os.path.isdir(nombre):
                shutil.rmtree(nombre)
                print(f"[−] Carpeta eliminada: {nombre}")

# Ejecutar todo
def main():
    print("Iniciando proceso de creación del ejecutable...")

    instalar_pyinstaller()

    print("[ ] El archivo PY a procesar debe estar en la carpeta 'base'.")
    print("[ ] El ejecutable se generará en la carpeta 'dist'.")
    option = input("[?] ¿Continuar? (s/n): ").strip().lower()
    if option != 's':
        print("[X] Proceso cancelado por el usuario.")
        exit(0)

    crear_ejecutable()
    limpiar_directorio()
    print("\n[✓] Tarea completada, saliendo en 5 segundos...")
    time.sleep(5)

if __name__ == "__main__":
    main()
