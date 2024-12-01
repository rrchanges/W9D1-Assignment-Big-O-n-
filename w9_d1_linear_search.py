def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    array = [10, 23, 45, 70, 11, 15]
    target1 = 70
    target2 = 11
    target3 = 99

    print(f"Index of {target1}: {linear_search(array, target1)}")
    print(f"Index of {target2}: {linear_search(array, target2)}")
    print(f"Index of {target3}: {linear_search(array, target3)}")

if __name__ == '__main__':
    main()