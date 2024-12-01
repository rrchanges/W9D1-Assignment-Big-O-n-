def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

def bubble_sort_optimized(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr



if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90 ]
    print(f"Sorted array: {bubble_sort(array)}")

    array = [5, 1, 4, 2, 8]
    print(f"Sorted array: {bubble_sort_optimized(array)}")
