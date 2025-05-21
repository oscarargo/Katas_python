
#1.- Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
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

# Cómo lo usaríamos
texto = "Hola caracola"
resultado = contar_frecuencias(texto)
print(resultado)

#2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    """
    Filtra las palabras de una lista que contienen la palabra objetivo.

    :param lista_palabras: Lista de palabras.
    :param palabra_objetivo: Palabra a buscar dentro de las palabras de la lista.
    :return: Lista de palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Como se usaría
palabras = ["manzana", "banana", "naranja", "mandarina", "sandia"]
objetivo = "man"
resultado = filtrar_palabras(palabras, objetivo)
print(resultado)#1.- Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
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

# Cómo lo usaríamos
texto = "Hola caracola"
resultado = contar_frecuencias(texto)
print(resultado)

#2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    """
    Filtra las palabras de una lista que contienen la palabra objetivo.

    :param lista_palabras: Lista de palabras.
    :param palabra_objetivo: Palabra a buscar dentro de las palabras de la lista.
    :return: Lista de palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Como se usaría
palabras = ["manzana", "banana", "naranja", "mandarina", "sandia"]
objetivo = "man"
resultado = filtrar_palabras(palabras, objetivo)
print(resultado)