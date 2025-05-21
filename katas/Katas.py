
#
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

# Duplicar valores en una lista usando map()
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)


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