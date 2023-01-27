def insertion_sort(arr):

    for i in range(1, len(arr)):
        current = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

    return arr


array = [23, 13, 23, 56, 47, 86, 24]
result = insertion_sort(array)
print(result)
