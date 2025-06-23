import subprocess
import sys
import os
import time
import shutil

# Verificar si pyinstaller está instalado
def instalar_pyinstaller():
    try:
        import PyInstaller  # noqa
    except ImportError:
        print("[+] PyInstaller no encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    else:
        print("[✓] PyInstaller ya está instalado.")

# Crear el ejecutable
def crear_ejecutable():
    script_path = os.path.join("base", "main.py")
    if not os.path.exists(script_path):
        print(f"[X] No se encontró el archivo {script_path}")
        sys.exit(1)

    print(f"[+] Creando ejecutable desde {script_path} ...")
    subprocess.run(["pyinstaller", "--onefile", script_path])

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
        sys.exit(0)
    crear_ejecutable()
    limpiar_directorio()
    print("\n[✓] Tarea completada, saliendo en 5 segundos...")
    time.sleep(5)

if __name__ == "__main__":
    main()
