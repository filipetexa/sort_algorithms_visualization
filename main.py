import random
import time
import sys

from sorting_algorithms.sorting_algorithms import *
from copy import deepcopy

# Definir parametros iniciais
ARRAY_SIZE = 1000
SAMPLE_RANGE = range(1000)

# Define um limit de recursao alto para que o merge sort não apresente stack overflow
sys.setrecursionlimit(len(SAMPLE_RANGE)**2)

"""
Instancia um Array de Array's randomicamete com base no parametro inicial
O primeiro array vai ter 2 elementos o segundo 3 e o ultimo n, sendo n o parametro inical
Exemplo:
n = 4
[[10, 20], [10, 20, 30], [10, 20, 30, 40], [10, 20, 30, 40, 50]]
"""
def generate_randon_array(array_size):
    # verifica se o input é um inteiro
    if not isinstance(array_size, int):
        raise Exception(f"{array_size} needs to be a int.")
    
    arr = []
    # loop on the size of the array
    for size in range(array_size):
        aux_arr = [random.choice(SAMPLE_RANGE) for _ in range(size + 2)]
        arr.append(aux_arr)
    return arr


randon_arr = generate_randon_array(ARRAY_SIZE)

# Generate deepcopies of the original randon array with the samples of arrays.
randon_arr_sort = deepcopy(randon_arr) 
randon_arr_bubble = deepcopy(randon_arr) 
randon_arr_merge = deepcopy(randon_arr)


for arr in randon_arr:
    print(selection_sort_algorithm(arr))
    # bubble_sort_algorithm(arr)
    # merge_sort_algorithm(arr)
    
    
# Call visualization function 

