# Projeto Sort Algorithms Visualization Python

## Descrição

Este projeto tem como objetivo implementar e visualizar a performance de diferentes algoritmos de ordenação, utilizando multithreading para executar os algoritmos simultaneamente em diferentes threads. O objetivo final é permitir que qualquer pessoa clone este repositório e execute o projeto em sua própria máquina, podendo visualizar em tempo real a eficiência de cada algoritmo em diferentes condições.
### Links de referencia
1. [Historia e Teoria](https://en.wikipedia.org/wiki/Sorting_algorithm)
2. [GeeksforGeeks](https://www.geeksforgeeks.org/sorting-algorithms/)

### Funcionalidades:

- Implementação de múltiplos algoritmos de ordenação (ex.: Bubble Sort, Merge Sort, Quick Sort, etc.).
- Execução simultânea dos algoritmos em threads separadas.
- Visualização em tempo real da performance de cada algoritmo utilizando ferramentas como Grafana ou outra solução de monitoramento.
- Modularização do código para facilitar a adição de novos algoritmos de ordenação no futuro.

## Estrutura do Projeto

- `sorting_algorithms/`: Diretório onde estarão os algoritmos de ordenação implementados.
- `visualization/`: Scripts e configurações para visualização dos tempos de execução em tempo real.
- `decorators`: Diretorio com funções de decoração que ajudam a tornar as funções do codigo mais genericas
- `utils`: Scripts com funções gerais
- `Output`: Diretorio onde os resultados do script são salvos ( ele é criado automaticamente pelo script)
- `main.py`: Script principal para iniciar a execução dos algoritmos e iniciar a visualização.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.

# data visualization
--plotly.express 
    https://dash.plotly.com/tutorial


## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/filipetexa/sort_algorithms_visualization.git
cd sort_algorithms_visualization
pip install -r requirements.txt

