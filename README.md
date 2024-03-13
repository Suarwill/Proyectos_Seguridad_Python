# Proyectos Python

## Generador de Contraseñas Aleatorias

Este sencillo script en Python genera contraseñas aleatorias de la longitud especificada por el usuario. Utiliza caracteres alfanuméricos y de puntuación para crear contraseñas robustas y seguras.

### Uso

1. Ejecuta el script en un entorno de Python.
2. Ingresa la longitud deseada para la contraseña cuando se solicite.
3. La contraseña generada se mostrará en la consola.


## Escaneador de Puertos por IP

Este proyecto de Python es un escaneador de puertos que permite al usuario elegir entre un escaneo rápido o completo de una dirección IP especificada. Proporciona información sobre los puertos abiertos y realiza un seguimiento del progreso durante el escaneo.

### Uso

1. Ejecuta el script en un entorno de Python.
2. Selecciona entre un escaneo rápido (r) o completo (c) cuando se solicite.
3. Tomará la IP del archivo "Lista IP.txt" y solicitará ingresar el tiempo de espera en segundos.
4. El script mostrará los puertos abiertos y el progreso del escaneo.
5. Se guardará los resultados en documento para su posterior análisis.


## Descifrador Hash

Este código en Python utiliza la librería hashlib para comparar un hash de contraseña con las contraseñas en un diccionario y encontrar la coincidencia.

### Descripción del Código

- **Contraseña en Hash:** Se proporciona una contraseña codificada en hash (`contraseñaEnHash`) que se va a comparar con las contraseñas en el diccionario.

- **Diccionario:** El código lee un diccionario de contraseñas desde un archivo de texto (`diccionario.txt`), donde cada línea representa una contraseña.

- **Búsqueda en el Diccionario:** Utiliza un bucle para iterar a través del diccionario y calcular el hash de cada contraseña. Si encuentra una coincidencia, imprime la contraseña original.

- **Resultado:** Al final, el código imprime si la contraseña se encontró en el diccionario y muestra cuántas contraseñas se exploraron en total.

### Uso Ético y Legal

Este código debería utilizarse éticamente y legalmente, obteniendo permisos y autorizaciones adecuadas antes de realizar pruebas de seguridad en sistemas.

## Encriptador

Script en Python, utilizando la libreria "Cryptodome".
Con este archivo encriptamos y desencriptamos archivos, la Key la lee del archivo 'key.txt' y el Vector de inicializacion del 'IV.txt'.
Aun en mejoras, pero tengo un buen avance en esta área.

### Uso

1. Ejecuta el script en un entorno de Python.
2. Ingresa la opcion Encriptar o Desencriptar.
3. Pedirá el nombre del archivo a realizar la accion anterior.