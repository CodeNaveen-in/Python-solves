"""
This script demonstrates and explains classic algorithms in Python:
- Binary Search
- Bubble Sort
- Merge Sort
- Dijkstra's Algorithm

Each section includes a brief explanation and a working example.
"""

# === 1. Binary Search ===
def binary_search(arr, target):
    """
    Binary Search: Efficiently finds the target in a sorted list.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
sorted_list = [1, 3, 5, 7, 9, 11]
print("🔍 Binary Search:", binary_search(sorted_list, 7))  # Output: 3


# === 2. Bubble Sort ===
def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
unsorted = [64, 34, 25, 12, 22, 11, 90]
print("🫧 Bubble Sort:", bubble_sort(unsorted))


# === 3. Merge Sort ===
def merge_sort(arr):
    """
    Merge Sort: Divide and conquer sorting algorithm.
    Time Complexity: O(n log n)
    """
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Example
unsorted = [38, 27, 43, 3, 9, 82, 10]
print("🧩 Merge Sort:", merge_sort(unsorted))


# === 4. Dijkstra's Algorithm ===
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm: Finds shortest paths from start node to all others.
    Time Complexity: O((V + E) log V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print("📍 Dijkstra's Shortest Paths:", dijkstra(graph, 'A'))