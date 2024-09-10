import random
import time
import sys
import os

from sorting_algorithms.sorting_algorithms import *
from copy import deepcopy

from decorators.decorators import \
apply_decorators_to_function, \
write_results_on_csv_file, \
get_execution_time

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

# Create output directory
base_output_path = './output' 
if not os.path.exists(base_output_path):
    os.makedirs(base_output_path)


# Create a decorated instance of the functions we need to use.
decorated_selection_sort_algorithm = apply_decorators_to_function(
    selection_sort_algorithm, 
    (write_results_on_csv_file, f'{base_output_path}/selection_sort_output.csv' ),  # Add decorator that insert the results into the output file
    get_execution_time  # Add decorator that gets the execution time 
)

decorated_bubble_sort_algorithm = apply_decorators_to_function(
    bubble_sort_algorithm, 
    (write_results_on_csv_file, f'{base_output_path}/bubble_sort_output.csv' ),  # Add decorator that insert the results into the output file
    get_execution_time  # Add decorator that gets the execution time 
)

decorated_merge_sort_algorithm = apply_decorators_to_function(
    merge_sort_algorithm, 
    (write_results_on_csv_file, f'{base_output_path}/merge_sort_output.csv' ),  # Add decorator that insert the results into the output file
    get_execution_time  # Add decorator that gets the execution time 
)

for arr in randon_arr:
    decorated_selection_sort_algorithm(arr)
    decorated_bubble_sort_algorithm(arr)
    decorated_merge_sort_algorithm(arr, left=0, right= len(arr) - 1)

    
    
# Call visualization function 

