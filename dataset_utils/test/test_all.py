# Importar los módulos
from dataset_utils.dataset import Dataset
from dataset_utils.discretization import *
from dataset_utils.metrics import *
from dataset_utils.preprocessing import *
from dataset_utils.filtering import *
from dataset_utils.correlation import *
from dataset_utils.visualization import *


# Cargar librerias
import random


###########################################
#                 DATASET                 #
###########################################

# Crear un objeto Dataset
dataset = Dataset()

# Leer datos desde un archivo
dataset = dataset.read_data('/home/mz/Mahaigaina/KISA/SME/Python/datasets/Student_bucketing.csv')

# Obtener los valores de un atributo específico
attribute_values = dataset.get_attribute('Age')

# Agregar un año a cada valor del atributo 'Age'
attribute_values = attribute_values + 1

# Establecer los valores actualizados en el atributo 'Age'
dataset.set_attribute('Age', attribute_values)

# Obtener el DataFrame de pandas que representa los datos del conjunto de datos
dataframe = dataset.get_data()
print(dataframe)

# Generar valores aleatorios de notas del curso
course_grades = [random.uniform(0, 10) for _ in range(len(dataset.get_attribute('Age')))]

# Agregar el atributo 'Course_Grade' al conjunto de datos
dataset.add_attribute('Course_Grade', course_grades)

# Generate random binary values (0 or 1)
bin = [random.choice([0, 1]) for _ in range(len(dataset.get_attribute('Age')))]
dataset.add_attribute('Bin', bin)


dataframe = dataset.get_data()
print(dataframe)





###########################################
#              DISCRETIZACIÓN             #
###########################################

# Discretizar el dataset utilizando el método de igual frecuencia
discretized_dataset = discretize_dataset(dataset, num_bins=5, method='equal_frequency')





###########################################
#              MÉTRICAS                   #
###########################################

# Calcular la varianza de un atributo no continuo
variance = calculate_attribute_variance(dataset,'Age')
print("Varianza de 'edad':", variance)

# Calcular la varianza de un atributo continuo
variance = calculate_attribute_variance(dataset,'Course_Grade')
print("Varianza de 'Course_Grade':", variance)


# Calcular la entropía de un atributo no discreto
entropy = calculate_attribute_entropy(dataset,'Course_Grade')
print("Entropía de 'Course_Grade':", entropy)

# Calcular la entropía de un atributo discreto
entropy = calculate_attribute_entropy(dataset,'Grade')
print("Entropía de 'Grade':", entropy)


# Calcular la entropía de un atributo discreto
entropy = calculate_attribute_entropy(dataset,'Age')
print("Entropía de 'Age':", entropy)

# Calcular el AUC del atributo 'edad' en relación al atributo de clase 'Bin'
auc = calculate_attribute_auc(dataset,'Age', 'Bin')
print("AUC de 'edad':", auc)




###########################################
#     NORMALIZACIÓ Y ESTANDARIZACIÓN      #
###########################################

# Normalizar un atributo
grade = dataset.get_attribute('Course_Grade')
grade_normalizado = normalize_variable(grade)

# Estandarización un atributo
grade = dataset.get_attribute('Course_Grade')
grade_estandarizado = standardize_variable(grade)

# Normalizar el dataset completo
dataset_normalizado = normalize_dataset(dataset)

# Estandarización del dataset completo
dataset_estandarizado = standardize_dataset(dataset)





###########################################
#         FILTRADO DE VARIABLES           #
###########################################

# Filtrar variables basado en la entropía mayor que 1
filtered_dataset = filter_variables(dataset, 'entropy', 1, '>')
# Mostrar las variables filtradas
print("Filtrado Entropia")
print(filtered_dataset.get_attributes())

# Filtrar variables basado en la varianza mayor que 1
print("Filtrado Varianza")
filtered_dataset = filter_variables(dataset, 'variance', 1, '>')
# Mostrar las variables filtradas
print(filtered_dataset.get_attributes())

# Filtrar variables basado en la auc mayor que 1
print("Filtrado AUC")
filtered_dataset = filter_variables(dataset, 'auc', 1, '>','Bin' )
# Mostrar las variables filtradas
print(filtered_dataset.get_attributes())





###########################################
#               CORRELACIÓN               #
###########################################

# Calcular la matriz de correlación
atributo1 = "Age"
atributo2 = "marks"
correlation_matrix = calculate_correlation(dataset, atributo1, atributo2)
print(f'La correlación entre {atributo1} y {atributo2} es: {correlation_matrix}')

matrix = calculate_correlation_matrix(dataset)
print(matrix)


###########################################
#               VISUALIZACIÓN             #
###########################################

# Graficar la matriz de correlación
plot_correlation_matrix(matrix)

# Graficar la entropia de Age y  Marks, 
entropy_values = []

entropy_values.append(calculate_attribute_entropy(dataset,'Age'))
entropy_values.append(calculate_attribute_entropy(dataset,'marks'))
plot_entropy(entropy_values, ['Age', 'marks'])

# Graficar la entropia de Age
variance_values = []
variance_values.append(calculate_attribute_variance(dataset,'Course_Grade'))
variance_values.append(calculate_attribute_variance(dataset,'Course_Grade'))
plot_entropy(variance_values, ['Course_Grade', 'Course_Grade'])

#Gracicar el AUC del atributo 'edad' en relación al atributo de clase 'Bin'
#plot_auc(auc)
plot_auc_roc(dataset, 'Age', 'Bin')
