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
    return enumerate(arr)

def bubble_sort_algorit_algorithm(list):
    
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]

    return list
            

# Cria o executor para trabalharmos com paralelismo
# Chama as threds executoras para executor os algorimos de ordenação

# Lista temporaria para testarmos o codigo do algoritimo aqui no arquivo main mesmo.
test_list = [10,13,2,9,7]
print(test_list)

print(bubble_sort_algorit_algorithm(test_list))


# Algoritimo 2 - Bubble Sort 


# Algoritimo 3
# Chama thread de visualição de dados.


