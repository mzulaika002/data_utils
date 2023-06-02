# Importar las librerías necesarias
import pandas as pd
from dataset_utils.dataset import Dataset
from dataset_utils.correlation import calculate_correlation

# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'edad': [25, 32, 41, 35, 28, 46, 38, 29, 33, 27, 31, 37, 39, 44, 30],
    'altura':[165.2, 170.5, 182.1, 175.7, 168.9, 190.3, 174.6, 169.8, 171.2, 167.5, 170.1, 178.6, 179.4, 185.0, 172.8],
    'ingresos': [50000, 60000, 75000, 80000, 55000, 90000, 65000, 70000, 62000, 48000, 58000, 62000, 78000, 85000, 54000],
    'color_de_pelo': ['rubio', 'castaño', 'castaño', 'rubio', 'rubio', 'castaño', 'moreno', 'castaño', 'rubio', 'castaño', 'rubio', 'castaño', 'rubio', 'castaño', 'moreno'],
    'estado_civil': ['soltero', 'casado', 'casado', 'soltero', 'soltero', 'casado', 'divorciado', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'soltero', 'casado', 'divorciado'],
    'fuma': [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})

# Crear un objeto Dataset
dataset = Dataset(data)

# Seleccionar dos atributos para calcular la correlación o información mutua
atributo1 = "edad"
atributo2 = "ingresos"

# Calcular la correlación o información mutua entre los atributos seleccionados
correlacion = calculate_correlation(dataset, atributo1, atributo2)

atributo1 = "color_de_pelo"
atributo2 = "estado_civil"
correlacion = calculate_correlation(dataset, atributo1, atributo2)

# Imprimir el resultado
print(f"La correlación entre '{atributo1}' y '{atributo2}' es: {correlacion}")

