from functools import wraps
import time
import csv

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
        
        return {'execution_time': execution_time, 'result': result}
    return wrapper


# escreve o resultado das funções em um arquivo csv
def write_results_on_csv_file(file_path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            
            with open(file_path, 'a', newline='') as csvfile:
                fieldnames = list(data.keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Verifica se o arquivo está vazio para escrever o cabeçalho
                csvfile.seek(0, 2)  # Move para o final do arquivo
                if csvfile.tell() == 0:
                    writer.writeheader()

                writer.writerow(data)
            return data
        return wrapper
    return decorator

def apply_decorators_to_function(func, *decorators):
    # Aplicar cada decorador em ordem inversa
    for decorator in reversed(decorators):
        if isinstance(decorator, tuple):  # Verifica se é um decorador parametrizado
            func = decorator[0](*decorator[1:])(func)
        else:  # Decorador simples
            func = decorator(func)
    return func

