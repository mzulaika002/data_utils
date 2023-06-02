import pandas as pd
from dataset_utils.dataset import Dataset
from dataset_utils.preprocessing import normalize_variable, standardize_variable, normalize_dataset, standardize_dataset


# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'edad': [25, 32, 41, 35, 28, 46, 38, 29, 33, 27, 31, 37, 39, 44, 30],
    'altura':[165.2, 170.5, 182.1, 175.7, 168.9, 190.3, 174.6, 169.8, 171.2, 167.5, 170.1, 178.6, 179.4, 185.0, 172.8],
    'ingresos': [50000, 60000, 75000, 80000, 55000, 90000, 65000, 70000, 62000, 48000, 58000, 62000, 78000, 85000, 54000],
    'gastos_mensuales': [4000, 5000, 6000, 5500, 4500, 7000, 5500, 6000, 5000, 4000, 4500, 5500, 6500, 7500, 4500],
    'estado_civil': ['soltero', 'casado', 'casado', 'soltero', 'soltero', 'casado', 'divorciado', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'divorciado'],
    'fuma': [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})

# Crear objeto Dataset a partir del DataFrame
dataset = Dataset(data)

# Normalización de un atributo individual
edad = dataset.get_attribute('fuma')
edad_normalizado = normalize_variable(edad)
print("Edad normalizado:", edad_normalizado)

# Estandarización de un atributo individual
ingresos = dataset.get_attribute('ingresos')
ingresos_estandarizado = standardize_variable(ingresos)
print("Ingresos estandarizado:", ingresos_estandarizado)

# Normalización del dataset completo
dataset_normalizado = normalize_dataset(dataset)
print("Dataset normalizado:")
print(dataset_normalizado.get_data())

# Estandarización del dataset completo
dataset_estandarizado = standardize_dataset(dataset)
print("Dataset estandarizado:")
print(dataset_estandarizado.get_data())




dataset_estandarizado = standardize_dataset(data)
print("Dataset estandarizado:")
print(dataset_estandarizado)