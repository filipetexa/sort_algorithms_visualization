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

# Algoritimo 1 - Selection Sort Algorithm - O(n log n)
def selection_sort_algorithm(list):
    min_value_position = 0
    
    list_size = len(list) - 1
    # Algoritimo
    for i, item in enumerate(list):
        
        aux_i = i + 1
        min_value_position = i
        
        while aux_i <= list_size:
            # Verifica se o valor de atual é o valor minimo 
            if list[min_value_position] > list[aux_i]:
                # Segura a posição do menor  valor
                min_value_position = aux_i
                
            # aux_i ++
            aux_i += 1
        list[i], list[min_value_position] = list[min_value_position], list[i]
        print(list)
    return list


# Cria o executor para trabalharmos com paralelismo
# Chama as threds executoras para executor os algorimos de ordenação

# Lista temporaria para testarmos o codigo do algoritimo aqui no arquivo main mesmo.
test_list = [random.choice(range(100)) for _ in range(10)]
print(test_list)


    


# Algoritimo 2
# Algoritimo 3
# Chama thread de visualição de dados.

selection_sort_algorithm(test_list)

