
# Algoritimo 1 - Selection Sort Algorithm - O(n log n)
def selection_sort_algorithm(arr):
    min_value_position = 0
    arr_size = len(arr) - 1
    for i, item in enumerate(arr):
        aux_i = i + 1
        min_value_position = i
        while aux_i <= arr_size:
            # Verifica se o valor de atual é o valor minimo 
            if arr[min_value_position] > arr[aux_i]:
                # Segura a posição do menor  valor
                min_value_position = aux_i
            # aux_i ++
            aux_i += 1
        arr[i], arr[min_value_position] = arr[min_value_position], arr[i]
    return arr

# Algoritimo 2 - Bubble Sort Algorithm - O(n^2)
def bubble_sort_algorithm(arr):
    
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_algorithm(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort_algorithm(arr, left, mid)
        merge_sort_algorithm(arr, mid + 1, right)
        merge(arr, left, mid, right)


"""
=============================================
"""
# def print_list(arr):
#     for i in arr:
#         print(i, end=" ")
#     print()

# # Driver code
# if __name__ == "__main__":
    # arr = [12, 11, 8, 13, 5, 6, 7]
    # print("Given array is")
    # print_list(arr)

    # merge_sort_algorithm(arr, 0, len(arr) - 1)

    # print("\nSorted array is")
    # print_list(arr)
    
    # result = selection_sort_algorithm([10,9,8,7,6,5,4,3,2,1])
    
    