def linear_search(arr, key):
    '''It returns the index of key. if not found, it returns -1'''
    '''Time: O(n) | Space: O(1)'''

    for index, item in enumerate(arr):
        if (item == key):
            return index

    return -1


arr = [23, 54, 16, 74, 82, 91]
key = 16
result = linear_search(arr, key)
print(result)
