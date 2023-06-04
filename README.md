# data_utils

-----

`data_utils` es un paquete de Python que proporciona funciones y utilidades para la gestión de datasets. Este paquete ha sido desarrollado como parte de la asignatura _Software matemático y estadístico_ del master KISA de EHU/UPV.

## Funcionalidades

Las principales funcionalidades implementadas en este paquete son:

- **Discretización**: Algoritmos de discretización para un solo atributo y para un dataset completo, utilizando el método de igual frecuencia e igual anchura.
- **Métricas**: Cálculo de métricas como la varianza y el AUC (para variables continuas) y la entropía (para variables discretas).
- **Normalización y estandarización**: Funciones para normalizar y estandarizar variables, tanto de manera individual como para el dataset completo.
- **Filtrado de variables**: Obtención de un nuevo dataset donde todas las variables cumplan ciertos requisitos definidos por las métricas implementadas.
- **Correlación**: Cálculo de la correlación (o información mutua para variables categóricas) por pares entre las variables de un dataset.
- **Visualización**: Plots para representar el AUC y las matrices de correlación/información mutua.


## Requisitos

- Python 
- Paquetes adicionales:

  - numpy
  - pandas
  - seaborn
  - math
  - matplotlib

## Instalación

Puedes instalar `data_utils` utilizando pip:

    pip install data_utils
    
Módulo de python instalable que facilite la distribución del software desarrollado en la carpeta `dist`

    pip install dist/dataset_utils-0.1.0.tar.gz
  
o

    pip install dist/dataset_utils-0.1.0-py3-none-any.whl
