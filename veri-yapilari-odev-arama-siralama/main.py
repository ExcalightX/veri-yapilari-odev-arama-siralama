from search_algorithms import linear_search, binary_search
from sort_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort


arr = [10, 7, 3, 8, 2, 5]

print("Orijinal dizi:", arr)

# SIRALAMA
print("\n--- SIRALAMA ALGORİTMALARI ---")
print("Bubble Sort:", bubble_sort(arr.copy()))
print("Selection Sort:", selection_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Merge Sort:", merge_sort(arr.copy()))
print("Quick Sort:", quick_sort(arr.copy()))

# ARAMA
sorted_arr = sorted(arr)

print("\n--- ARAMA ALGORİTMALARI ---")
print("Linear Search (8):", linear_search(arr, 8))
print("Binary Search (8):", binary_search(sorted_arr, 8))
