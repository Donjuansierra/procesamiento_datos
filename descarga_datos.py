import requests
import csv


# Funcion para descargar datos de una Url
def descarga_datos(url, nombre):
    """
    Función para descargar datos de una url especifica
    
    parametros:
    url --> dirección web en la cual se encuentran los datos
    nombre --> nombre del archivo a crear, se debe recordar que debe terminar en .csv
    **todos los parametros a insertar deben ir en comillas
    
    """
    
    # Para leer el request como texto
    response = requests.get(url) 
        
    # Para leer el request como texto
    data = response.text
        
    # Para crea un archivo CSV con el nombre especificado y escribir datos en el csv
    with open(nombre, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in data.split("\n"):
            writer.writerow(row.split(","))
    return nombre


# Prueba de la función
datos = descarga_datos("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv", "dataset.csv")

print(datos)



