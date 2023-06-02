from dataset_utils.metrics import *
import pandas as pd


# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'edad': [25, 32, 41, 35, 28, 46, 38, 29, 33, 27, 31, 37, 39, 44, 30],
    'altura':[165.2, 170.5, 182.1, 175.7, 168.9, 190.3, 174.6, 169.8, 171.2, 167.5, 170.1, 178.6, 179.4, 185.0, 172.8],
    'ingresos': [55000, 60000, 70000, 80000, 55000, 90000, 65000, 70000, 62000, 48000, 58000, 62000, 78000, 85000, 54000],
    'estado_civil': ['soltero', 'casado', 'casado', 'soltero', 'soltero', 'casado', 'divorciado', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'divorciado'],
    'fuma': [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})

# Crear un objeto Dataset
dataset = Dataset(data)

# Calcular la varianza del atributo 'ingresos'
variance = calculate_attribute_variance(dataset, 'ingresos')
print("Varianza de 'ingresos':", variance)

# Calcular la varianza del atributo 'altura'
entropy = calculate_attribute_variance(dataset, 'altura')
print("Varianza de 'altura':", entropy)

# Calcular la entropía del atributo 'ingresos'
entropy = calculate_attribute_entropy(dataset, 'ingresos')
print("Entropía de 'ingresos':", entropy)

# Calcular la entropía del atributo 'estado_civil'
entropy = calculate_attribute_entropy(dataset, 'estado_civil')
print("Entropía de 'estado_civil':", entropy)

# Calcular la entropía del atributo 'altura'
entropy = calculate_attribute_entropy(dataset, 'altura')
print("Entropía de 'altura':", entropy)

# Calcular el AUC del atributo 'edad' en relación al atributo de clase 'fuma'
auc = calculate_attribute_auc(dataset, 'edad', 'fuma')
print("AUC de 'edad':", auc)


