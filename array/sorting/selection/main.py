def selection_sort(arr):
    arrLen = len(arr)

    for i in range(arrLen):

        for j in range(i+1, arrLen):
            if (arr[j] < arr[i]):
                arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [23, 65, 16, 73, 41, 31, 99, 6]
result = selection_sort(arr)
print(result)
