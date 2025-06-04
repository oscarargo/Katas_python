
#1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias(cadena):
    """
    Recibe una cadena de texto y devuelve un diccionario con las frecuencias de cada letra.
    Los espacios no son considerados.
    """
    frecuencias = {}
    for letra in cadena.replace(" ", ""):  # Elimina los espacios
        letra = letra.lower()  # Convierte a minúsculas para un conteo uniforme
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias

# Ejemplo de uso
texto = "Hola caracola"
resultado = contar_frecuencias(texto)
print(resultado)

# 2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# Duplicar valores en una lista usando map()
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

# 3  Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo
def filtrar_palabras(lista_palabras, palabra_objetivo):
    """
    Filtra las palabras de una lista que contienen la palabra objetivo.

    :param lista_palabras: Lista de palabras.
    :param palabra_objetivo: Palabra a buscar dentro de las palabras de la lista.
    :return: Lista de palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Ejemplo de uso
palabras = ["manzana", "banana", "naranja", "mandarina", "sandia"]
objetivo = "man"
resultado = filtrar_palabras(palabras, objetivo)
print(resultado)

# 4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencia(lista1,lista2):
    """
    calcula la diferencia entre los valores de dos listas.
    usa la función map()
    1. Convierte las listas a conjuntos para eliminar duplicados.
    2. Convierte los conjuntos a listas.
    3. Usa la función map() para calcular la diferencia entre los valores de las listas.

    Args:
        lista1 (_type_): _description_
        lista2 (_type_): _description_
    """
    lista1= list(set(lista1))
    lista2= list(set(lista2))
    return list(map(lambda x,y:x-y,lista1,lista2))
# Como usaríamos la función
lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
resultado= calcular_diferencia(lista1,lista2)
print (resultado)

#5  Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def calcular_media_y_estado(lista_numeros, nota_aprobado=5):
    """
    Calcula la media de una lista de números y determina si es mayor o igual que la nota de aprobado.
    la función devuelve una tupla con la media y el estado ("aprobado" o "suspenso")
    1. Calcula la media de los números en la lista.
    2. Compara la media con la nota de aprobado.
    3. Devuelve una tupla con la media y el estado.
    4. Si la lista está vacía, devuelve (0, "suspenso")
    5. Si la lista contiene un solo número, devuelve ( número,"aprobado" o "suspenso")
)

    Args:
        lista_numeros (_type_): _description_
        nota_aprobado (int, optional): _description_. Defaults to 5.
    """
    if not lista_numeros:
        return (0,"suspenso")
    if len(lista_numeros)==1:
        return (lista_numeros[0], "aprobado" if lista_numeros[0] >=nota_aprobado else "suspenso")
    media=sum(lista_numeros)/len(lista_numeros)
    estado="aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)
# como lo usaríamos
lista_numeros= [0,1,7,8,9]
resultado= calcular_media_y_estado(lista_numeros)
print(resultado)

# 6 Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.
    1. Si n es 0 o 1, devuelve 1.
    2. De lo contrario, devuelve n * factorial(n-1).
   
    Args:
        n (_type_): _description_
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Ejemplo de uso

numero = 5
resultado = factorial(numero)
print(f"el factorial de {numero} es {resultado}")


#7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def convertir_tuplas_a_strings ( lista_tuplas):
    """
    Convierte una lista de tuplas a una lista de strings.
    1. Usa la función map() para convertir cada tupla en un string.
    2. Usa la función join() para unir los elementos de cada tupla en un string.
    3. Devuelve la lista de strings.
    """
    return list(map(lambda x:" ".join(x), lista_tuplas))

# Como lo usaríamos
lista_tuplas=[("hola","mundo"),("adios","mundo")]
resultado= convertir_tuplas_a_strings(lista_tuplas)
print(resultado)

#8 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def dividir_numeros():
    """
    Pide al usuario dos números e intenta dividirlos.
    Maneja excepciones para valores no numéricos y división por cero.
    1. Pide al usuario que ingrese dos números.
    2.Intenta dividir los números.
    3. Si la división es exitosa, muestra el resultado.
    4. Si hay una excepción, muestra un mensaje de error.
    """
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"La división fue exitosa. El resultado es: {resultado}")


#9 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def filtrar_mascotas_prohibidas(lista_mascotas):
    """
    Filtra una lista de nombres de mascotas excluyendo las mascotas prohibidas en España.
    1. Define una lista de mascotas prohibidas.
    2- Usa la función filter() para filtrar las mascotas que no están en la lista de prohibidas.
    3.- Devuelve la lista filtrada.

    Args:
        lista_mascotas (_type_): _description_
    """
    mascotas_prohibidas = ["Mapache", "Tigre", " Serpiente Pitón", " Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))
#como lo usaríamos
lista_mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
resultado = filtrar_mascotas_prohibidas(lista_mascotas)
print ( resultado)

# 10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def promedio(lista):
    if not lista:
        raise ValueError("La lista está vacía.")
    return sum(lista) / len(lista)

try:
    print(promedio([10, 20, 30]))
    print(promedio([]))
except ValueError as e:
    print("Error:", e)

# 11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("Edad fuera del rango permitido.")
except ValueError as e:
    print("Error:", e)
else:
    print("Edad válida:", edad)

#12 Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    """
    Devuelve una lista con la longitud de cada palabra en la frase.

    Args:
        frase (_type_): _description_

    Returns:
        _type_: _description_
    """
    return list(map(len, frase.split()))

# Ejemplo
print(longitud_palabras("Hola mundo esto es Python"))

# 13 Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(conjunto):
    """
    Devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas.
    
    """
   
    conjunto = set(conjunto)  # Elimina duplicados
    return list(map(lambda x: (x.upper(), x.lower()), conjunto))
#Ejemplo
conjunto = "abcde"
resultado = letras_mayus_minus(conjunto)
print (resultado)

#14 Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter().
def palabras_con_letra(lista_palabras, letra):
    """
    Filtra las palabras de una lista que comienzan con una letra específica.
    1.Usa la función filter() para filtrar las palabras que comienzan con la letra especificada.
    2. Devuelve la lista filtrada.
    3. Convierte la letra a minúsculas para una comparación uniforme.
    4. Convierte la lista filtrada a una lista normal.

    Args:
        lista_palabras (_type_): _description_
        letra (_type_): _description_
    """
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
#Ejemplo
lista_palabras = ["manzana", "banana", "naranja", "mandarina", "sandia"]
letra= "m"
resultado = palabras_con_letra(lista_palabras, letra)
print(resultado)

#15 Crea una función lambda que  sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Ejemplo
print(sumar_tres([1, 2, 3, 4]))

# 16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas(texto, n):
    return list(filter(lambda x: len(x) > n, texto.split()))

# Ejemplo
print(palabras_largas("Este es un ejemplo de oración", 4))

#17 Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()
from functools import reduce
def lista_a_numero(lista_digitos):
    """
    Convierte una lista de dígitos en un número entero.
    1. Usa la función reduce() para combinar los dígitos en un solo número.
    2. Convierte cada dígito a string y únelos.
    3. Convierte el resultado a un número entero.

    Args:
        lista_digitos (_type_): _description_
    """
    return int(reduce(lambda x, y: str(x) + str(y), lista_digitos))
#Ejemplo
lista_digitos = [5, 7, 2]
resultado = lista_a_numero(lista_digitos)
print(resultado)  

#18 Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def filtrar_estudiantes(estudiantes):
    """
    Filtra una lista de estudiantes y devuelve aquellos con calificación mayor o igual a 90.
    1. Usa la función filter() para filtrar los estudiantes con calificación >= 90.
    2.Devuelve la lista filtrada.

    Args:
        estudiantes (_type_): _description_
    """
    return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))
# ejemplo
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Pedro", "edad": 21, "calificacion": 90},
    {"nombre": "Maria", "edad": 19, "calificacion": 92}
]
resultado = filtrar_estudiantes(estudiantes)
print (resultado)

# 19 Crea una función lambda que filtre los números impares de una lista dada.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# La lambda devuelve True si el número es impar, False si es par
filtro_impares = lambda numero: numero % 2 != 0

numeros_impares = list(filter(filtro_impares, numeros))

print("Lista original de números:", numeros)
print("Números impares filtrados:", numeros_impares)

#20 Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def filtrar_enteros(lista):
    """
    Filtra una lista y devuelve solo los elementos de tipo entero.
    1. Usa la función filter() para filtrar los elementos de tipo int.
    2. Devuelve la lista filtrada.

    Args:
        lista (_type_): _description_
    """
    return list(filter(lambda x: isinstance(x, int), lista))
# como se usaría la función:
lista_mixta = [1, "dos", 3, "cuatro", 5, "seis"]
resultado = filtrar_enteros(lista_mixta)
print("Lista original:", lista_mixta)
print("Lista filtrada de enteros:", resultado)

#21 Crea una función que calcule el cubo de un número dado mediante una función lambda

# La lambda toma 'numero' como entrada y devuelve 'numero' elevado a la potencia de 3
cubo = lambda numero: numero ** 3

# Probar la función lambda con algunos números
num1 = 2
num2 = 5
num3 = 10

print(f"El cubo de {num1} es: {cubo(num1)}")
print(f"El cubo de {num2} es: {cubo(num2)}")
print(f"El cubo de {num3} es: {cubo(num3)}")

# 22 Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().
from functools import reduce
def producto_total(lista_numeros):
    """
    Calcula el producto total de los valores en una lista numérica.
    1. Usa la función reduce() para multiplicar todos los números de la lista.
    2. Devuelve el producto total.

    Args:
        lista_numeros (_type_): _description_
    """
    return reduce(lambda x, y: x * y, lista_numeros)
# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
resultado = producto_total(lista_numeros)
print(f"El producto total de la lista {lista_numeros} es: {resultado}")

#23 Concatena una lista de palabras.Usa la función reduce().
def concatenar_palabras(lista_palabras):
    """
    Concatena una lista de palabras en una sola cadena.
    1. Usa la función reduce() para unir todas las palabras en una sola cadena.
    2. Devuelve la cadena resultante.

    Args:
        lista_palabras (_type_): _description_
    """
    return reduce(lambda x, y: x + " " + y, lista_palabras)
# Ejemplo de uso
lista_palabras = ["Hola", "mundo", "esto", "es", "Python"]
resultado = concatenar_palabras(lista_palabras)
print(f"La concatenación de la lista {lista_palabras} es: '{resultado}'")

# 24 Calcula la diferencia total en los valores de una lista. Usa la función reduce().

def diferencia_total(lista_numeros):
    """
    Calcula la diferencia total de los valores en una lista numérica.
    1. Usa la función reduce() para restar todos los números de la lista.
    2. Devuelve la diferencia total.

    Args:
        lista_numeros (_type_): _description_
    """
    return reduce(lambda x, y: x - y, lista_numeros)

# Ejemplo de uso
lista_numeros = [10, 2, 3, 1]
resultado = diferencia_total(lista_numeros)
print(f"La diferencia total de la lista {lista_numeros} es: {resultado}")

#25 Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    """
    Cuenta el número de caracteres en una cadena de texto.
    1. Usa la función len() para contar los caracteres.
    2. Devuelve el número total de caracteres.

    Args:
        cadena (str): Cadena de texto a analizar.
    """
    return len(cadena)
# Ejemplo de uso
texto = "Hola, mundo!"
resultado = contar_caracteres(texto)
print(f"El número de caracteres en la cadena '{texto}' es: {resultado}")

#26 Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda x, y: x % y
# Ejemplo de uso
x = 10
y = 3
resultado = resto_division(x, y)
print(f"El resto de la división entre {x} y {y} es: {resultado}")

#27 Crea una función que calcule el promedio de una lista de números.
# Definir la función para calcular el promedio
def calcular_promedio(lista_numeros):
    """
    Calcula el promedio (media aritmética) de una lista de números.

    Parámetros:
        lista_numeros (list): Una lista de números (enteros o flotantes).

    Retorna:
        float: El promedio de los números en la lista.
        str: Un mensaje de error si la lista está vacía.
    """
    if not lista_numeros:  # Comprobar si la lista está vacía
        return "La lista está vacía, no se puede calcular el promedio."

    total_suma = sum(lista_numeros)  # Suma todos los números en la lista
    cantidad_numeros = len(lista_numeros) # Obtiene la cantidad de números

    promedio = total_suma / cantidad_numeros # Calcula el promedio

    return promedio

# Probar la función con diferentes listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30]
lista3 = [7]
lista4 = []
lista5 = [2.5, 3.5, 4.0]

print(f"El promedio de {lista1} es: {calcular_promedio(lista1)}")
print(f"El promedio de {lista2} es: {calcular_promedio(lista2)}")
print(f"El promedio de {lista3} es: {calcular_promedio(lista3)}")
print(f"El promedio de {lista4} es: {calcular_promedio(lista4)}")
print(f"El promedio de {lista5} es: {calcular_promedio(lista5)}")

# 28 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada
def primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento duplicado en una lista.
    1. Usa un conjunto para rastrear los elementos vistos.
    2. Itera sobre la lista y devuelve el primer elemento que ya ha sido visto.

    Args:
        lista (list): Lista de elementos a analizar.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # Si no hay duplicados
# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 3, 6]
resultado = primer_duplicado(lista)
if resultado is not None:
    print(f"El primer elemento duplicado en la lista {lista} es: {resultado}")
else : 
    print(f"No hay elementos duplicados en la lista {lista}")


#29 Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro
def enmascarar_cadena(cadena):
    """
    Convierte una variable en una cadena de texto y enmascara todos los caracteres con '#', excepto los últimos cuatro.
    1. Convierte la variable a cadena de texto.
    2. Reemplaza todos los caracteres excepto los últimos cuatro con '#'.
    3. Devuelve la cadena enmascarada.

    Args:
        cadena (str): La cadena a enmascarar.
    """
    cadena_str = str(cadena)
    if len(cadena_str) <= 4:
        return cadena_str  # No se enmascara si la longitud es menor o igual a 4
    return '#' * (len(cadena_str) - 4) + cadena_str[-4:]

#como lo usaríamos
cadena = "1234567890"
resultado = enmascarar_cadena(cadena)
print(f"La cadena enmascarada de '{cadena}' es: '{resultado}'")

#30 Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden
def son_anagramas(palabra1, palabra2):
    """
    Determina si dos palabras son anagramas.
    1. Convierte ambas palabras a minúsculas y ordena sus letras.
    2. Compara las palabras ordenadas.

    Args:
        palabra1 (str): Primera palabra.
        palabra2 (str): Segunda palabra.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
# Ejemplo de uso
palabra1 = "amor"
palabra2 = "roma"
resultado = son_anagramas(palabra1, palabra2)
if resultado:
    print(f"'{palabra1}' y '{palabra2}' son anagramas.")
else:
    print(f"'{palabra1}' y '{palabra2}' no son anagramas.")


#31 Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre_en_lista():
    """
    Solicita al usuario ingresar una lista de nombres y busca un nombre específico.
    Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado.
    Si no está, lanza una excepción.
    """
    nombres = input("Ingrese una lista de nombres separados por comas: ").split(",")
    nombre_a_buscar = input("Ingrese el nombre a buscar: ").strip()

    if nombre_a_buscar in nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
# Ejemplo de uso
try:
    buscar_nombre_en_lista()
except ValueError as e:
    print("Error:", e)

# 32 Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre_completo, lista_empleados):
    """
    Busca un nombre completo en una lista de empleados y devuelve su puesto.
    Si el nombre no está en la lista, devuelve un mensaje indicando que no trabaja aquí.

    Args:
        nombre_completo (str): Nombre completo del empleado a buscar.
        lista_empleados (list): Lista de diccionarios con información de empleados.

    Returns:
        str: Puesto del empleado o mensaje indicando que no trabaja aquí.
    """
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo:
            return f"{empleado['nombre']} trabaja como {empleado['puesto']}."
    return f"{nombre_completo} no trabaja aquí."
# Ejemplo de uso
lista_empleados = [
    {"nombre": "Juan Pérez", "puesto": "Desarrollador"},
    {"nombre": "Ana Gómez", "puesto": "Diseñadora"},
    {"nombre": "Luis Fernández", "puesto": "Gerente"}
]
nombre_a_buscar = "Ana Gómez"
resultado = buscar_empleado(nombre_a_buscar, lista_empleados)
print(resultado)

# 33 Crea una función lambda que sume elementos correspondientes de dos listas dadas
suma_elementos = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = suma_elementos(lista1, lista2)
print(f"La suma de los elementos correspondientes de {lista1} y {lista2} es: {resultado}")

""" 34 Crea la clase 
Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco , 
nueva_rama , 
crecer_ramas , 
quitar_rama e 
info_arbol . El objetivo es implementar estos métodos para 
manipular la estructura del árbol.
 Código a seguir:
 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 2. Implementar el método 
crecer_tronco para aumentar la longitud del tronco en una unidad.
 3. Implementar el método 
nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 4. Implementar el método 
crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 5. Implementar el método 
quitar_rama para eliminar una rama en una posición específica.
 6. Implementar el método 
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
mismas.
 Caso de uso:
 1. Crear un árbol.
 2. Hacer crecer el tronco del árbol una unidad.
 3. Añadir una nueva rama al árbol.
 4. Hacer crecer todas las ramas del árbol una unidad.
 5. Añadir dos nuevas ramas al árbol.
 6. Retirar la rama situada en la posición 2.
 7. Obtener información sobre el árbol.
 """
class Arbol:
    def __init__(self):
        self.tronco = 1  # Longitud inicial del tronco
        self.ramas = []  # Lista de ramas

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina una rama en una posición específica."""
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("Posición inválida para eliminar la rama.")

    def info_arbol(self):
        """Devuelve información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas."""
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
# Caso de uso
arbol = Arbol()
arbol.crecer_tronco()  # Hacer crecer el tronco una unidad
arbol.nueva_rama()  # Añadir una nueva rama al árbol
arbol.crecer_ramas()  # Hacer crecer todas las ramas del árbol una unidad
arbol.nueva_rama()  # Añadir otra nueva rama al árbol
arbol.nueva_rama()  # Añadir una tercera nueva rama al árbol
arbol.quitar_rama(2)  # Retirar la rama situada en la posición 2
info = arbol.info_arbol()  # Obtener información sobre el árbol
print(f"Información del árbol: {info}")

""" 35 Crea la clase 
UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
agregar dinero al saldo.
 Código a seguir:
  Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
 Implementar el método True y False .

 Retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no 
poder hacerse.

  Implementar el método 
transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
Lanzará un error en caso de no poder hacerse.

 Implementar el método 
agregar_dinero para agregar dinero al saldo del usuario.

 Caso de uso:
 Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 Agregar 20 unidades de saldo de "Bob".
 Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
  Retirar 50 unidades de saldo a "Alicia".
 """
class UsuarioBanco:
    def __init__(self, nombre, saldo_inicial, tiene_cuenta_corriente):
        """
        Inicializa un usuario con su nombre, saldo y si tiene o no cuenta corriente.
        
        Args:
            nombre (str): Nombre del usuario.
            saldo_inicial (float): Saldo inicial del usuario.
            tiene_cuenta_corriente (bool): Indica si el usuario tiene cuenta corriente.
        """
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.tiene_cuenta_corriente = tiene_cuenta_corriente
    def retirar_dinero(self, cantidad):
        """
        Retira dinero del saldo del usuario.
        
        Args:
            cantidad (float): Cantidad a retirar.
        
        Raises:
            ValueError: Si la cantidad es mayor que el saldo o si no tiene cuenta corriente.
        """
        if not self.tiene_cuenta_corriente:
            raise ValueError("No se puede retirar dinero sin cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para retirar esta cantidad.")
        self.saldo -= cantidad
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Realiza una transferencia desde otro usuario al usuario actual.
        
        Args:
            otro_usuario (UsuarioBanco): Usuario desde el cual se realiza la transferencia.
            cantidad (float): Cantidad a transferir.
        
        Raises:
            ValueError: Si la cantidad es mayor que el saldo del otro usuario o si no tiene cuenta corriente.
        """
        if not otro_usuario.tiene_cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene cuenta corriente para realizar transferencias.")
        if cantidad > otro_usuario.saldo:
            raise ValueError("Saldo insuficiente en el usuario que transfiere.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
    def agregar_dinero(self, cantidad):

        """
        Agrega dinero al saldo del usuario.
        
        Args:
            cantidad (float): Cantidad a agregar al saldo.
        """
        self.saldo += cantidad
# Caso de uso
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)
usuario2.agregar_dinero(20)  # Agregar 20 unidades de saldo a "Bob"
usuario1.transferir_dinero(usuario2, 80)  # Transferir 80 unidades de "Bob" a "Alicia"
usuario1.retirar_dinero(50)  # Retirar 50 unidades de saldo a "Alicia"


""" 36   Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabra, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir pirmero y llamar dentro de la función procesar_texto.

Código a seguir:
1.- Crear una función contar_palabras para contar el número de veces que aparece cada palabra en un texto. Tiene que devolver un diccionario
2.- Crear una función reemplazar_palabra para reemplazar una palabra_original del texto por una palabra_nueva. tiene que devolver el texto con el reemplazo de palabras.
3.- Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
4.- Crear la función procesar_texto que tome un textso, una opción ( entre "contar", "reemplazar", "eliminar") y un número de argumentos variable segun la opción indicada.

Caso de uso:

comprueba el funcionamiento completo de la función procesar_texto.
"""
def contar_palabras(texto):
    """
    Cuenta el número de veces que aparece cada palabra en un texto.
    
    Args:
        texto (str): Texto a procesar.
    
    Returns:
        dict: Diccionario con palabras como claves y sus conteos como valores.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo
def reemplazar_palabra(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra original en el texto por una nueva.
    
    Args:
        texto (str): Texto a procesar.
        palabra_original (str): Palabra a reemplazar.
        palabra_nueva (str): Nueva palabra que reemplazará a la original.
    
    Returns:
        str: Texto con la palabra reemplazada.
    """
    return texto.replace(palabra_original, palabra_nueva)
def eliminar_palabra(texto, palabra):
    """
    Elimina una palabra del texto.
    
    Args:
        texto (str): Texto a procesar.
        palabra (str): Palabra a eliminar.
    
    Returns:
        str: Texto con la palabra eliminada.
    """
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra]
    return ' '.join(palabras)
def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción especificada.
    
    Args:
        texto (str): Texto a procesar.
        opcion (str): Opción de procesamiento ("contar", "reemplazar", "eliminar").
        *args: Argumentos adicionales según la opción.
    
    Returns:
        dict o str: Resultado del procesamiento según la opción.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se requieren dos argumentos para reemplazar: palabra_original y palabra_nueva.")
        return reemplazar_palabra(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se requiere un argumento para eliminar: palabra.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Debe ser 'contar', 'reemplazar' o 'eliminar'.")
# Ejemplo de uso
texto = "Hola mundo, este es un texto de prueba. Hola mundo."
try:
    print("Contar palabras:", procesar_texto(texto, "contar"))
    print("Reemplazar palabra:", procesar_texto(texto, "reemplazar", "Hola", "Adiós"))
    print("Eliminar palabra:", procesar_texto(texto, "eliminar", "mundo"))
except ValueError as e:
    print("Error:", e)

    

# 37 Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario
def determinar_periodo_dia(hora):
    """
    Determina si es de noche, de día o tarde según la hora proporcionada.
    
    Args:
        hora (int): Hora en formato 24 horas (0-23).
    
    Returns:
        str: "Noche", "Día" o "Tarde".
    """
    if 0 <= hora < 6:
        return "Noche"
    elif 6 <= hora < 12:
        return "Día"
    elif 12 <= hora < 18:
        return "Tarde"
    elif 18 <= hora < 24:
        return "Noche"
    else:
        return "Hora inválida"
# Ejemplo de uso
try:
    hora_usuario = int(input("Ingrese la hora (0-23): "))
    periodo = determinar_periodo_dia(hora_usuario)
    print(f"Es {periodo}.")

except ValueError:
    print("Error: Debe ingresar un número entero entre 0 y 23.")

"""# 38  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
Las reglas de calificación son:
 de 0 a 69 insuficiente
 de 70 a 79 bien
 de 80 a 89 muy bien
 de 90 a 100 excelente
 """
def calificacion_texto(calificacion):
    """
    Determina la calificación en texto según la calificación numérica.
    
    Args:
        calificacion (int): Calificación numérica (0-100).
    
    Returns:
        str: Calificación en texto.
    """
    if 0 <= calificacion < 70:
        return "Insuficiente"
    elif 70 <= calificacion < 80:
        return "Bien"
    elif 80 <= calificacion < 90:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "Calificación inválida"
# Ejemplo de uso
try:
    calificacion_usuario = int(input("Ingrese la calificación numérica (0-100): "))
    resultado = calificacion_texto(calificacion_usuario)
    print(f"La calificación es: {resultado}")
except ValueError:
    print("Error: Debe ingresar un número entero entre 0 y 100.")

#39 Escribe una función que tome dos parámetros: "triangulo" ) y figura (una cadena que puede ser "rectangulo" , "circulo" o datos (una tupla con los datos necesarios para calcular el área de la figura)
def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica según el tipo de figura y los datos proporcionados.
    
    Args:
        figura (str): Tipo de figura ("triangulo", "rectangulo", "circulo").
        datos (tuple): Datos necesarios para calcular el área.
    
    Returns:
        float: Área de la figura.
    """
    if figura == "triangulo":
        base, altura = datos
        return 0.5 * base * altura
    elif figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return 3.14159 * radio ** 2
    else:
        raise ValueError("Figura no válida. Debe ser 'triangulo', 'rectangulo' o 'circulo'.")
# Ejemplo de uso
try:
    figura_usuario = input("Ingrese la figura (triangulo, rectangulo, circulo): ").strip().lower()
    if figura_usuario == "triangulo":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        datos = (base, altura)
    elif figura_usuario == "rectangulo":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        datos = (base, altura)
    elif figura_usuario == "circulo":
        radio = float(input("Ingrese el radio del círculo: "))
        datos = (radio,)
    else:
        raise ValueError("Figura no válida.")
    
    area = calcular_area(figura_usuario, datos)
    print(f"El área de la figura es: {area}")
except ValueError as e:
    print("Error:", e)

""" #40  En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
siguiente:
 1. Solicita al usuario que ingrese el precio original de un artículo.
 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python
"""
def calcular_precio_final():
    """
    Calcula el precio final de una compra en una tienda en línea después de aplicar un descuento.
    """
    try:
        precio_original = float(input("Ingrese el precio original del artículo: "))
        tiene_cupon = input("¿Tiene un cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí":
            valor_cupon = float(input("Ingrese el valor del cupón de descuento: "))
            if valor_cupon <= 0:
                raise ValueError("El valor del cupón debe ser mayor a cero.")
            precio_final = precio_original - valor_cupon
        else:
            precio_final = precio_original

        print(f"El precio final de la compra es: {precio_final:.2f}€")
    except ValueError as e:
        print("Error:", e)
# Ejemplo de uso
calcular_precio_final()

