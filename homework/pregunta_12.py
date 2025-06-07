"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "../files/input/data.csv")
    suma_por_letra = {}
    with open(data_path, "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valores_col5 = [int(par.split(':')[1]) for par in columns[4].split(',')]
            suma = sum(valores_col5)
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma
    return dict(sorted(suma_por_letra.items()))
print(pregunta_12())