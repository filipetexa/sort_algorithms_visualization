# Arquivo de teste: test_decorators.py

from .decorators import write_results_on_csv_file
import pytest
import csv

# Teste unitário para o decorator write_results_on_csv_file
def test_write_results_on_csv_file(tmpdir):
    # Cria um arquivo temporário para o CSV
    temp_file = tmpdir.join("output.csv")

    # Função de exemplo que retorna dados a serem escritos no CSV
    @write_results_on_csv_file(temp_file.strpath)  # Passa o caminho do arquivo temporário para o decorador
    def sample_function():
        return {"name": "John", "age": "30", "city": "New York"}

    # Chama a função decorada, que deve escrever no arquivo CSV
    sample_function()

    # Lê o conteúdo do arquivo CSV
    with open(temp_file, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        csv_content = list(reader)

    # Verifica se o conteúdo do CSV corresponde ao que foi retornado pela função
    expected_row = {"name": "John", "age": "30", "city": "New York"}

    assert len(csv_content) == 1  # Verifica se há uma linha
    assert csv_content[0] == expected_row  # Verifica se a linha corresponde ao esperado
