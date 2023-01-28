def reverse(arr):
    arrLen = len(arr)

    # In each loop, swapping nth element with arr[len(arr) - (n + 1)]  n >= 0
    for i in range(arrLen//2):
        # syntax for swapping values of two variables
        arr[i], arr[arrLen - (i + 1)] = arr[arrLen - (i + 1)], arr[i]

    return arr


array = [57, 28, 19, 64, 92, 47]
result = reverse(array)
print(result)
