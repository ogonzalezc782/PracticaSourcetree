import pandas as pd
import numpy as np
import math

df = pd.read_csv("diabetes.csv")
print("Dimensión de la tabla:", df.shape)

# Función que retorna el menor de tres valores
def menor(A, B, C):
    return min(A, B, C)

# Función que retorna el maximo de 3 valores
def maximo(A, B, C):
    return max(A, B, C)
