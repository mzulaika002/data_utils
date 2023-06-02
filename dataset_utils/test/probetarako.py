# CARGAR FUNCIONES DE OTROS FICHEROS -------------------------------------------
from dataset_utils.dataset import Dataset
from dataset_utils.metrics import *


# CREAR DATASET DE PRUEBA ------------------------------------------------------
dataset = Dataset()
dataset.add_attribute("A", [1, 2, 3, 4, 5])
dataset.add_attribute("B", [2, 4, 6, 8, 10])
dataset.add_attribute("C", [3, 6, 9, 12, 15])

# DEFINIR MÉTRICA Y UMBRAL -----------------------------------------------------
metric = 'variance'
threshold = 5.0

# APLICAR FILTRADO ------------------------------------------------------------
filtered_dataset = filter_variables(dataset, metric, threshold)

# RESULTADOS -------------------------------------------------------------------
print("Atributos originales:", dataset.get_attributes())
print("Datos originales:")
print(dataset.get_data())

print("\nAtributos filtrados:", filtered_dataset.get_attributes())
print("Datos filtrados:")
print(filtered_dataset.get_data())
