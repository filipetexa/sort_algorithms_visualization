

# Algoritimo 1 - Selection Sort Algorithm - O(n log n)
def selection_sort_algorithm(list):
    min_value_position = 0
    list_size = len(list) - 1
    for i in enumerate(list):
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
    return list