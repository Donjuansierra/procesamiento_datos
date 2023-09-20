from datasets import load_dataset
import numpy as np
import pandas as pd

# cargue de información
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

''' # Conversión de columna age en arreglo NumPy y se halla edad promedio
arr_age = np.array(data['age'])
avg_age = arr_age.mean()
print('La edad promedio de los pacientes es: ', avg_age) '''

# Convertir la estructura Dataset en un DataFrame de Pandas

df = pd.DataFrame(data)

# Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento

df_a = df[df['is_dead'] == 0].copy() # alive
df_d = df[df['is_dead'] == 1].copy() # dead

# Calcular los promedios de las edades de cada dataset e imprimir

avg_age_a = df_a['age'].mean()
avg_age_d = df_d['age'].mean()

print(f'La edad promedio de los pacientes vivos es: {avg_age_a}')
print(f'La edad promedio de los pacientes muertos es: {avg_age_d}')
