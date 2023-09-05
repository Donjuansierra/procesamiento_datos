from datasets import load_dataset
import numpy as np

# cargue de información
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Conversión de columna age en arreglo NumPy y se halla edad promedio
arr_age = np.array(data['age'])
avg_age = arr_age.mean()
print('La edad promedio de los pacientes es: ', avg_age)




