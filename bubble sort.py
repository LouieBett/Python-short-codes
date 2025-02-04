def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the sorting process
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break

# Example usage
if __name__ == '__main__':
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)

    bubble_sort(sample_list)

    print("Sorted list:", sample_list)