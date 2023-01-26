def merge(arr):
    '''returns sorted array without mutating passed one'''
    '''Time: nlog(n) | Space: O(n)'''

    arrLen = len(arr)  # current array length

    if arrLen == 1:  # array of one element is sorted array
        return arr

    # for array of 1+ length, sort their left and right half and store in respective variable
    sortedLeft = merge(arr[: arrLen // 2])
    sortedRight = merge(arr[arrLen // 2:])

    # merge the above two sorted array in a sorted way into this new array
    sortedArray = []

    # Procedure to merge
    indexLeft = 0  # keep track of index of first element of left slice
    indexRight = 0  # same for right slice

    # loop until all elements of any of them are put in sortedArray
    while indexLeft < len(sortedLeft) and indexRight < len(sortedRight):
        if (sortedLeft[indexLeft] < sortedRight[indexRight]):
            sortedArray.append(sortedLeft[indexLeft])
            indexLeft += 1
        else:
            sortedArray.append(sortedRight[indexRight])
            indexRight += 1

    # procedure to put remaining elements into sortedArray of either left or right slice
    if indexLeft == len(sortedLeft):
        for i in range(indexRight, len(sortedRight)):
            sortedArray.append(sortedRight[i])

    if indexRight == len(sortedRight):
        for j in range(indexLeft, len(sortedLeft)):
            sortedArray.append(sortedLeft[j])

    return sortedArray


arr = [23, 65, 47, 15, 75, 17, 87, 23]

result = merge(arr)
print(result)
print(arr)
