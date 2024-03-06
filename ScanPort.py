import socket
import time
import datetime

def _init_():
    print("¿Desea realizar un escaneo rápido (r) o completo (c)?")

    user_option = input("(r) ó (c): ")

    host = socket.gethostname()
    mi_ip = socket.gethostbyname(host)

    print(f"Tu dirección IP es: {mi_ip}")

    # Leer las IP's desde el archivo "Lista IP"
    with open("Lista IP.txt", "r") as file:
        ips = file.read().splitlines()

    for ip in ips:
        latencia = int(input(f"Indique tiempo de espera en segundos para la IP {ip} (se recomienda 3): "))

        if user_option == "c":
            scanCompleto(ip, latencia)
        elif user_option == "r":
            scanRapido(ip, latencia)
        else:
            print("Elija una opción válida.")

def guardar_resultados(ip, puertos_abiertos):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"resultados_{ip}_{timestamp}.txt"

    with open(nombre_archivo, "w") as file:
        file.write(f"Resultados del escaneo para la IP: {ip}\n")
        file.write("Puertos abiertos:\n")
        for puerto in puertos_abiertos:
            file.write(f"{puerto}\n")

def scanCompleto(ip, latencia):
    puertosAbiertos = []
    for puerto in range(1, 65536):
        puertoEscaneado = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        puertoEscaneado.settimeout(latencia)

        resultado = puertoEscaneado.connect_ex((ip, puerto))

        if resultado == 0:
            print("Puerto Abierto: ", puerto)
            puertosAbiertos.append(puerto)

        puertoEscaneado.close()
        time.sleep(0.1)

        if puerto % 100 == 0:
            progreso = str(round(puerto * 0.001525 , 2))
            print("Escaneado " + progreso + "%")

    guardar_resultados(ip, puertosAbiertos)
    print("Escaneados todos los puertos")
    print("En el IP: ", ip)
    print("Los puertos encontrados son: ")
    print(puertosAbiertos)

def scanRapido(ip, latencia):
    puertosComunes = [
    21, 22, 23, 25, 53, 80, 110, 123, 137, 138, 139, 143, 161, 194, 389, 443,
    445, 465, 514, 515, 548, 587, 631, 636, 993, 995, 1080, 1433, 1521, 1723,
    1883, 2049, 2181, 2375, 2376, 3306, 3389, 4000, 4200, 4369, 4500, 5000,
    5432, 5672, 5900, 5984, 6379, 6666, 6667, 6668, 6669, 8000, 8080, 8443,
    8888, 9090, 9200, 9418, 9999, 10000, 11211, 15672, 27017, 27018, 27019,
    50000, 50030, 50070, 50470, 54321, 60000, 62078, 64738, 65000, 65129,
    65130, 65131, 65132, 65133, 65134, 65135, 65136, 65137, 65138, 65139,
    65140, 65141, 65142, 65143, 65144, 65145, 65146, 65147, 65148, 65149,
    65150, 65500, 65501, 65502, 65503, 65504, 65505, 65506, 65507, 65508,
    65509, 65510, 65511, 65512, 65513, 65514, 65515, 65516, 65517, 65518,
    65519, 65520, 65521, 65522, 65523, 65524, 65525, 65526, 65527, 65528,
    65529, 65530, 65531, 65532, 65533, 65534, 65535 
    ]
    puertosAbiertos = []

    for puerto in puertosComunes:
        puertoEscaneado = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        puertoEscaneado.settimeout(latencia)

        resultado = puertoEscaneado.connect_ex((ip, puerto))

        if resultado == 0:
            print("Puerto Abierto ---> : ", puerto)
            puertosAbiertos.append(puerto)

        puertoEscaneado.close()
        time.sleep(0.1)

    guardar_resultados(ip, puertosAbiertos)
    print("Escaneados todos los puertos")
    print("En el IP: ", ip)
    print("Los puertos encontrados son: ")
    print(puertosAbiertos)

_init_ = _init_()
