import time

# --- 1. Bubble Sort ---
# Time Complexity: O(n^2) - Simple but inefficient for large lists.

def bubble_sort(arr):
    """Sorts a list using the Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# --- 2. Selection Sort ---
# Time Complexity: O(n^2) - Finds the minimum element and places it at the beginning.

def selection_sort(arr):
    """Sorts a list using the Selection Sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- 3. Insertion Sort ---
# Time Complexity: O(n^2) average/worst case, O(n) best case (if already sorted).
# Efficient for small or nearly sorted datasets.

def insertion_sort(arr):
    """Sorts a list using the Insertion Sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- 4. Merge Sort ---
# Time Complexity: O(n log n) - A highly efficient, divide-and-conquer algorithm.

def merge_sort(arr):
    """Sorts a list using the Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Merge the two sorted halves
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr

# --- 5. Quick Sort ---
# Time Complexity: O(n log n) average case, O(n^2) worst case.
# Very fast in practice.

def quick_sort(arr):
    """Sorts a list using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# --- 6. Python's Built-in Sort (Timsort) ---
# Time Complexity: O(n log n) - Highly optimized hybrid of Merge Sort and Insertion Sort.

def python_sort(arr):
    """Uses Python's optimized built-in sort function (Timsort)."""
    arr.sort() # Sorts in-place
    # Alternatively: sorted_arr = sorted(arr)
    return arr

# --- Example Usage ---

if __name__ == "__main__":
    data_sample = [64, 25, 12, 22, 11, 90, 45, 3]

    print(f"Original list: {data_sample}\n")

    # Use .copy() so we can sort the original data sample with each function
    print(f"Bubble Sort:    {bubble_sort(data_sample.copy())}")
    print(f"Selection Sort: {selection_sort(data_sample.copy())}")
    print(f"Insertion Sort: {insertion_sort(data_sample.copy())}")
    # Note: Quick Sort implementation returns a new list, doesn't modify in-place
    print(f"Quick Sort:     {quick_sort(data_sample.copy())}") 
    print(f"Merge Sort:     {merge_sort(data_sample.copy())}")
    print(f"Python Built-in: {python_sort(data_sample.copy())}")
