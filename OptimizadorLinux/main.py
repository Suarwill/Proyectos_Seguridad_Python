import os
import subprocess
import sys

# --- CONFIGURACIÓN DE DEPENDENCIAS ---
DEPENDENCIAS = {
    "smartctl": "smartmontools",
    "deborphan": "deborphan",
    "zramctl": "zram-tools",
    "dmidecode": "dmidecode"
}

def check_and_install_dependencies():
    print("[*] Verificando dependencias del sistema...")
    for comando, paquete in DEPENDENCIAS.items():
        import shutil
        if shutil.which(comando) is None:
            print(f"[!] '{comando}' no encontrado. Instalando {paquete}...")
            try:
                subprocess.run(f"sudo apt update && sudo apt install -y {paquete}", shell=True, check=True)
                print(f"[+] {paquete} instalado correctamente.")
            except subprocess.CalledProcessError:
                print(f"[X] Error al intentar instalar {paquete}. Revisa tu conexión.")
        else:
            print(f"[OK] {comando} ya está instalado.")

def run_command(command, description):
    print(f"\n[+] {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Falló la ejecución de: {description}")

def setup_zram():
    print("\n--- Configuración de ZRAM (Optimización de RAM) ---")
    zram_config = "ALGO=lz4\nPERCENT=60\nPRIORITY=100\n"
    subprocess.run(f"echo '{zram_config}' | sudo tee /etc/default/zramswap", shell=True)
    run_command("sudo modprobe zram && sudo systemctl restart zramswap", "Activando ZRAM")

def main():
    check_and_install_dependencies()
    
    while True:
        print("\n" + "═"*55)
        print("      FRAUSTECH TOOLKIT v2.0 - OPTIMIZACIÓN KALI")
        print("═"*55)
        print(" 1. [INFO] Características del Notebook y CPU")
        print(" 2. [INFO] Salud del Disco Duro (S.M.A.R.T.)")
        print(" 3. [LIMPIEZA] Apt, Caché y Huérfanos (deborphan)")
        print(" 4. [LIMPIEZA] Logs del sistema (Journalctl)")
        print(" 5. [OPTIMIZAR] Configurar ZRAM y Swappiness=10")
        print(" 6. [SERVICIOS] DESACTIVAR carga de Docker/VirtualBox")
        print(" 7. [SERVICIOS] ACTIVAR Entorno (Docker/VBox) ahora")
        print(" 8. [ESTADO] Ver RAM, ZRAM y Swap actual")
        print(" 0. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                print("\n--- Información de Hardware ---")
                os.system("lscpu | grep -E 'Model name|CPU\(s\)|Thread'")
                os.system("sudo dmidecode -s system-product-name")
                os.system("sudo dmidecode -s system-manufacturer")
            
            case "2":
                run_command("sudo smartctl -H /dev/sda", "Verificando salud física del HDD")
            
            case "3":
                run_command("sudo apt clean && sudo apt autoremove --purge -y $(deborphan)", "Limpiando paquetes y huérfanos")
                run_command("rm -rf ~/.cache/*", "Limpiando caché de usuario")
            
            case "4":
                run_command("sudo journalctl --vacuum-size=200M", "Reduciendo logs a 200MB")
            
            case "5":
                setup_zram()
                swap_cmd = "echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf && sudo sysctl -p"
                run_command(swap_cmd, "Configurando Swappiness=10 permanente")
            
            case "6":
                servicios = "virtualbox.service docker.service docker.socket containerd.service"
                run_command(f"sudo systemctl disable {servicios}", "Desactivando servicios del arranque")
            
            case "7":
                run_command("sudo systemctl start docker virtualbox", "Iniciando servicios de trabajo")
            
            case "8":
                os.system("free -h && swapon --show && zramctl")
            
            case "0":
                print("Saliendo de Fraustech Toolkit...")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()