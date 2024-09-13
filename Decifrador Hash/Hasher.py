import hashlib as hl

# Contraseña codificada en HASH
contraseñaEnHash = "dbe9787aaf4002c6662e490b3f1f7512807459b6dee2e1c2e56738e1cbbd993c"

# Ubicacion del diccionario
archivoDiccionario = "diccionario.txt"

# Abriendo el diccionario
with open (archivoDiccionario, 'r') as file:
    diccionario = [line.strip() for line in file]
    contraseñaResuelta = ""
    contraseñasExploradas = 0
    # Cada opcion vamos transformando en HASH
    for cadena in diccionario:
        contraseñasExploradas += 1
        # La transformamos en hash y la comparamos con nuestro objetivo HASH buscado.
        calcularHash = hl.sha256(cadena.encode()).hexdigest()
        if calcularHash == contraseñaEnHash:
            contraseñaResuelta = cadena
            print("La contraseña es: ", contraseñaResuelta)
            break
        else:
            print("La contraseña no se encuentra en el diccionario.")
    print(f"Se exploraron {contraseñasExploradas} contraseñas en el diccionario.")
