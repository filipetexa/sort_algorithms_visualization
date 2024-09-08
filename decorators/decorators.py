from functools import wraps
import time

def get_execution_time(func):   
# # Exemplo de uso
# @get_execution_time
# def funcao_exemplo(x):
#     # Exemplo de função que faz algo que leva tempo
#     time.sleep(x)
#     return x * 2

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Inicia o cronômetro
        start_time = time.time()
        
        # Executa a função original
        result = func(*args, **kwargs)
        
        # Para o cronômetro
        end_time = time.time()
        
        # Calcula o tempo de execução
        execution_time = end_time - start_time
        
        return execution_time, result
    return wrapper

def write_results_on_csv_file(algorithm_name, arr_size, execution_time):
    ...