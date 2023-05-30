from setuptools import setup

setup(
   name='dataset_utils',
   version='0.0.1',
   author='Muitze Zulaika Gallastegi',
   author_email='mzulaika002@ikasle.ehu.eus',
   packages=['dataset_utils', 'dataset_utils.test'],
   #url='https://github.com/tu_usuario/data_utils...TODO',
   license='LICENSE.txt',
   description='Paquete de Python para la gestión de datasets',
   long_description=open('README.txt').read(),
   tests_require=['pytest'],
   install_requires=[
      "seaborn >= 0.9.0",
      "pandas >= 0.25.1",
      "numpy >=1.17.2"
   ],
   python_requires='>=3.6',
)