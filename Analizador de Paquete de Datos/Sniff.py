# En PAUSA (hasta tener mejor PC)

"""
from scapy.all import sniff, IP

def packet_callback(packet):
    # Lógica de análisis
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Filtrado por dirección IP sospechosa
        suspicious_ip = 'IP_sospechosa'
        if ip_src == suspicious_ip or ip_dst == suspicious_ip:
            # Generar alerta o tomar medidas
            print("¡Alerta! Actividad sospechosa detectada:")
            print(f"   - Paquete: {packet.summary()}")
            print(f"   - Fuente IP: {ip_src}, Destino IP: {ip_dst}")

# Captura de paquetes en tiempo real
sniff(prn=packet_callback, store=0)
"""