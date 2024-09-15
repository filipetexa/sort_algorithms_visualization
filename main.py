
import time
import sys
import os

from sorting_algorithms.sorting_algorithms import *
from utils.array_functions import *
from copy import deepcopy

from decorators.decorators import \
apply_decorators_to_function, \
write_results_on_csv_file, \
get_execution_time


# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Definir parametros iniciais
ARRAY_SIZE = 1000
SAMPLE_RANGE = range(1000)

# Define um limit de recursao alto para que o merge sort não apresente stack overflow
sys.setrecursionlimit(len(SAMPLE_RANGE)**2)


# Create array withe the tests list to be sorted
# randon_arr = generate_randon_arrays(ARRAY_SIZE, SAMPLE_RANGE)
randon_arr = generate_worse_case_arrays_to_sort(ARRAY_SIZE)

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
# Read the output csv's and treat data
df_selection = pd.read_csv('output/selection_sort_output.csv')
df_selection['array_size'] = df_selection['result'].apply(lambda x: int(x[1:-1].split(',')[0]))
df_selection = df_selection[['execution_time', 'array_size']]
df_selection['algorithm'] = 'Selection Sort'

df_bubble = pd.read_csv('output/bubble_sort_output.csv')
df_bubble['array_size'] = df_bubble['result'].apply(lambda x: int(x[1:-1].split(',')[0]))
df_bubble = df_bubble[['execution_time', 'array_size']]
df_bubble['algorithm'] = 'Bubble Sort'

df_merge = pd.read_csv('output/merge_sort_output.csv')
df_merge['array_size'] = df_merge['result'].apply(lambda x: int(x[1:-1].split(',')[0]))
df_merge = df_merge[['execution_time', 'array_size']]
df_merge['algorithm'] = 'Merge Sort'

dfs = pd.concat([df_merge, df_selection, df_bubble])

# Initialize app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Sort Algorithms Visualization'),
    # grafico de linhas!!!!
    html.Div(children='SELECTION SORT'),
    dcc.Graph(figure=px.line(df_selection, x='array_size', y='execution_time')),
    html.Div(children='BUBBLE SORT'),
    dcc.Graph(figure=px.line(df_bubble, x='array_size', y='execution_time')),
    html.Div(children='MERGE SORT'),
    dcc.Graph(figure=px.line(df_merge, x='array_size', y='execution_time')),
    html.Div(children='COMPARAÇÃO'),
    dcc.Graph(figure=px.line(dfs, x='array_size', y='execution_time', color='algorithm')),
]

app.run(debug=False)
