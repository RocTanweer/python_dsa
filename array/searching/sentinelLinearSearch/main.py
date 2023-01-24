def sentinel_linear_search(arr, key):
    '''Time: O(n) | Space: O(1)'''

    # temporarily storing the last element
    last = arr[len(arr)-1]
    # replacing the last element with the key
    arr[len(arr)-1] = key

    index = 0

    # loop will terminate when key is found
    while (arr[index] != key):
        index += 1

    arr[len(arr)-1] = last

    # key is found only if the index is less than array length or the last element is the required element
    if (index < len(arr) - 1 or key == arr[len(arr) - 1]):
        return index
    else:
        return -1


array = [23, 543, 76, 87, 16, 97]
key = 97
result = sentinel_linear_search(array, key)
print(result)
