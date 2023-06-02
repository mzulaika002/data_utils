# Importar los módulos
from dataset_utils.dataset import *

# Crear un objeto Dataset vacio
ds = Dataset()

# Ayuda
ds.show_help()

# Leer datos desde un archivo
ds = ds.read_data('/home/mz/Mahaigaina/KISA/SME/Python/datasets/Student_bucketing.csv')

# Obtener el DataFrame del conjunto de datos
data = ds.get_data()
print(data)

# Crear un nuevo objeto Dataset
data = {
    'Nombre': ['Ane', 'Maider', 'Mikel'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Donostia', 'Iruña', 'Baiona']
    }
dataset = Dataset(data)

# Escribir datos en un archivo
dataset.write_data('data_output.csv')

# Leer datos desde un archivo
dataset.read_data('data_output.csv')

# Obtener el DataFrame de pandas que representa los datos del conjunto de datos
dataframe = dataset.get_data()
print(dataframe)
print()

# Obtener la lista de nombres de atributos
attribute_names = dataset.get_attributes()
print(attribute_names)
print()

# Obtener los valores de un atributo específico
attribute_values = dataset.get_attribute('Nombre')
print(attribute_values)
print()

# Establecer los valores de un atributo específico
set_values = [22, 20, 21]
dataset.set_attribute('Edad', set_values)
dataframe = dataset.get_data()
print(dataframe)
print()

# Establecer los valores de un nuevo atributo
dataset.add_attribute('Altura', [165.5, 170.2, 180.0])
dataframe = dataset.get_data()
print(dataframe)
print()


