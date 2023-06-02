from dataset_utils.discretization import *
import numpy as np

import random

x = [11.5, 10.2, 1.2, 0.5, 5.3, 20.5, 8.4]
# = [5, 10, 50, 72, 92, 104]
#x = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
#x = [ 4, 7, 13, 16, 20, 24, 27, 29, 31, 33, 38, 42]

x = np.array([11.5, 10.2, 1.2, 0.5, 5.3, 20.5, 8.4])

num_bins = 4

x_discretized, cut_points = discretizeEW(x, num_bins)
print("Equal Width ")
print("Valores discretizados:", x_discretized)
print("Puntos de corte:", cut_points)
print()

x_discretized, cut_points = discretizeEF(x, num_bins)
print("Equal Frequency ")
print("Valores discretizados:", x_discretized)
print("Puntos de corte:", cut_points)
print()

x_discretized = smooth_by_bin_boundaries(x, num_bins)
print("Smooth boundaries ")
print("Valores discretizados:", x_discretized)
print()

x_discretized = smooth_by_bin_mean(x, num_bins)
print("Smooth mean ")
print("Valores discretizados:", x_discretized)
print()

x_discretized = smooth_by_bin_median(x, num_bins)
print("Smooth median ")
print("Valores discretizados:", x_discretized)
print()



x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
num_bins = 3

x_discretized, cut_points = discretizeEW(x, num_bins)

print("Valores discretizados:", x_discretized)
print("Puntos de corte:", cut_points)



x = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
num_bins = 4

x_discretized, cut_points = discretizeEF(x, num_bins)

print("Valores discretizados:", x_discretized)
print("Puntos de corte:", cut_points)


x = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
num_bins = 4

x_discretized, cut_points = discretizeEF(x, num_bins)

print("Valores discretizados:", x_discretized)
print("Puntos de corte:", cut_points)


attribute = [5, 10, 15, 20, 25, 30, 35, 40]
num_bins = 2
method = 'equal_frequency'

discretized_attribute, cut_points = discretize_attribute(attribute, num_bins, method)

print("Atributo discretizado:", discretized_attribute)
print("Puntos de corte:", cut_points)



dataset = Dataset()
dataset = dataset.read_data('/home/mz/Mahaigaina/KISA/SME/Python/datasets/Student_bucketing.csv')
# Generar valores aleatorios de notas del curso
course_grades = [random.uniform(0, 10) for _ in range(len(dataset.get_attribute('Age')))]
# Agregar el atributo 'Course_Grade' al conjunto de datos
dataset.add_attribute('Course_Grade', course_grades)


num_bins = 3
method = 'equal_width'

discretized_dataset = discretize_dataset(dataset, num_bins, method)

# Imprimir dataset discretizados
print("Atributo discretizado:", discretized_dataset.get_data())

attribute = dataset.get_attribute('Course_Grade')
discretized_attribute = discretize_attribute(attribute, num_bins, method)
