import hashlib as hl

contraseñaEnHash = "dbe9787aaf4002c6662e490b3f1f7512807459b6dee2e1c2e56738e1cbbd993c"   # Contraseña codificada en hash
archivoDiccionario = "diccionario.txt"  # Ubicacion del diccionario

with open (archivoDiccionario, 'r') as file:
    diccionario = [line.strip() for line in file]
    contraseñaResuelta = ""
    contraseñasExploradas = 0
    for contraseña in diccionario:
        contraseñasExploradas += 1
        calcularHash = hl.sha256(contraseña.encode()).hexdigest()
        if calcularHash == contraseñaEnHash:
            contraseñaResuelta = contraseña
            break
    if calcularHash == contraseñaEnHash:
        print("La contraseña es: ", contraseñaResuelta)
    else:
        print("La contraseña no se encuentra en el diccionario.")
    print("Se exploraron " + str(contraseñasExploradas)+ " contraseñas en el diccionario.")