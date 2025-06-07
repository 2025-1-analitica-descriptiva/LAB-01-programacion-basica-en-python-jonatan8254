"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import os

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "../files/input/data.csv")
    valores = {}
    with open(data_path, "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valor = int(columns[1])
            if letra not in valores:
                valores[letra] = []
            valores[letra].append(valor)
    resultado = []
    for letra in sorted(valores.keys()):
        maximo = max(valores[letra])
        minimo = min(valores[letra])
        resultado.append((letra, maximo, minimo))
    return resultado
print(pregunta_05())