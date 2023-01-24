def bubble_sort(arr):
    '''Time: O(n**2) | Space: O(1)'''

    arrLen = len(arr)

    for i in range(arrLen):
        for j in range(0, arrLen - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [23, 76, 14, 68, 18, 34]
result = bubble_sort(arr)
print(result)
