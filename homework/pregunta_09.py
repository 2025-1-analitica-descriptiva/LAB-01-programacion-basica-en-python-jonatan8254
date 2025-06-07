"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



import os

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "../files/input/data.csv")
    conteo = {}
    with open(data_path, "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            claves = [par.split(':')[0] for par in columns[4].split(',')]
            for clave in claves:
                conteo[clave] = conteo.get(clave, 0) + 1
    return dict(sorted(conteo.items()))
print(pregunta_09())