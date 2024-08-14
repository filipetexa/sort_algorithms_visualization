import random

# Definir parametros iniciais
ARRAY_SIZE = 10
SAMPLE_RANGE = range(100000)


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


# Cria o executor para trabalharmos com paralelismo
# Chama as threds executoras para executor os algorimos de ordenação

# Algoritimo 1
# Algoritimo 2
# Algoritimo 3
# Chama thread de visualição de dados.

print(generate_randon_array(5))
