import random
import time

comparison_count = 0
swap_count = 0

def merge_sort(arr):
    global comparison_count, swap_count
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        swap_count += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

def quick_sort(arr):
    global comparison_count, swap_count
    
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)
    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    comparison_count += len(arr) - 1
    swap_count += len(lesser) + len(greater)
    
    return quick_sort(lesser) + equal + quick_sort(greater)

def selection_sort(arr):
    global comparison_count, swap_count
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swap_count += 1
    
    return arr

def measure_time_and_complexity(algorithm, arr):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0
    
    start_time = time.time()
    sorted_arr = algorithm(arr)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    print(f"{algorithm.__name__}: Sorted {len(sorted_arr)} elements in {execution_time:.6f} seconds.")
    print(f"Number of comparisons: {comparison_count}")
    print(f"Number of swaps: {swap_count}\n")

# Generate a random list of integers
arr = random.sample(range(1, 10000), 1000)

# Measure time and complexity for merge sort
measure_time_and_complexity(merge_sort, arr)

# Measure time and complexity for quick sort
measure_time_and_complexity(quick_sort, arr)

# Measure time and complexity for selection sort
measure_time_and_complexity(selection_sort, arr)
