import string, random

def generador(largo):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(caracteres, k=largo))

def main():
    while True:
        try:
            largo = int(input("Ingrese el largo de la contraseña aleatoria: "))
            if largo <= 0:
                print("La longitud debe ser un número positivo.")
            else:
                print("La contraseña aleatoria es:", generador(largo))
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()