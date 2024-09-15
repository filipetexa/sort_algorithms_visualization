import random

"""
Instancia um Array de Array's randomicamete com base no parametro inicial
O primeiro array vai ter 2 elementos o segundo 3 e o ultimo n, sendo n o parametro inical
Exemplo:
n = 4
[[10, 20], [10, 20, 30], [10, 20, 30, 40], [10, 20, 30, 40, 50]]
"""
def generate_randon_arrays(array_size, sample_range):
    # verifica se o input é um inteiro
    if not isinstance(array_size, int):
        raise Exception(f"{array_size} needs to be a int.")
    
    arr = []
    # loop on the size of the array
    for size in range(array_size):
        aux_arr = [random.choice(sample_range) for _ in range(size + 2)]
        arr.append(aux_arr)
    return arr


"""
Instancia um Array de Array's com o pior caso para uma ordenação
O primeiro array vai ter 2 elementos o segundo 3 e o ultimo n, sendo n o parametro inical
Exemplo:
n = 4
[[1, 0], [2, 1, 0], [3, 2, 1, 0], [4, 3, 2, 1, 0]]
"""
def generate_worse_case_arrays_to_sort(array_size):
    # verifica se o input é um inteiro
    if not isinstance(array_size, int):
        raise Exception(f"{array_size} needs to be a int.")
    arr = []
    # loop on the size of the array
    for size in range(array_size):
        aux_arr = [size + 2 - i for i in range(size + 2)]
        arr.append(aux_arr)
    return arr

