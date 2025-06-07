"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import fileinput
import glob
import os.path
def load_input(input_directory):
    
    files = glob.glob(f'{input_directory}/*')  #lee todo el conyenido de la carpeta input_directory con /*, si ponemos /*.txt solo leee los txt
    with fileinput.input(files = files) as f:  #Va a leer secuencialmente cada arcivo, el primer file es lo que espera la funcion y el segundo es mi variable
        sequence = [ (fileinput.filename(), line) for line in f ] #agrega ctuplas a la lista con el nombre del archivo como calve , y la linea como valor

    return sequence

         

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    # 1) Definimos la ruta donde están almacenados los archivos de entrada
    ruta = "files/input/"
    # 2) Cargamos todos los datos de esa ruta. 
    #    Se asume que load_input() devuelve un iterable de tuplas (archivo, línea)
    data = load_input(ruta)
    # 3) Inicializamos el acumulador de la suma
    suma = 0
    # 4) Recorremos cada par (nombre_del_archivo, línea_de_texto) en data
    for archive, line in data:
        #   a) 'strip()' elimina espacios o saltos de línea al inicio/final
        #   b) 'split("\t")' separa la línea en una lista usando tabulador como separador
        partes = line.strip().split("\t")
        #   c) Convertimos la segunda columna (índice 1) a entero y lo sumamos
        suma += int(partes[1])
    # 5) Devolvemos la suma total de la segunda columna de todas las líneas
    return suma

if __name__ == "__main__":
    # Cuando se ejecuta este archivo directamente, se llama a pregunta_01()
    # y se imprime su resultado en pantalla
    print(pregunta_01())