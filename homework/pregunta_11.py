"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "../files/input/data.csv")
    suma_por_letra = {}
    with open(data_path, "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            valor = int(columns[1])
            letras = columns[3].split(',')
            for letra in letras:
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    return dict(sorted(suma_por_letra.items()))
print(pregunta_11())