from .sorting_algorithms import merge_sort_algorithm, bubble_sort_algorithm, selection_sort_algorithm
import pytest

test_set = [
        (
            [10,9,8,7,6,5,4,3,2,1], 
            [1,2,3,4,5,6,7,8,9,10]
        ),
        (
            [10,9,8,7,50,5,4,3,2,1], 
            [1,2,3,4,5,7,8,9,10,50]
        )
]

@pytest.mark.parametrize('arr, result', test_set)
def test_sort_selection_algorithm(arr, result):
    assert selection_sort_algorithm(arr) == result

@pytest.mark.parametrize('arr, result', test_set)
def test_sort_bubble_algorithm(arr, result):
    assert bubble_sort_algorithm(arr) == result
    
@pytest.mark.parametrize('arr, result', test_set)
def test_sort_merge_algorithm(arr, result):
    left = 0
    right = len(arr) - 1 
    assert merge_sort_algorithm(arr, left, right) == result