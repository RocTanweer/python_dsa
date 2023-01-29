def left_rotate(arr, steps):

    arrLen = len(arr)

    while steps > 0:
        first = arr[0]  # Capturing the first element of the array

        for j in range(arrLen - 1):
            # Shifting the elements to left by assigning their value to previous elements
            arr[j] = arr[j + 1]

        # After loops ends, the last two elements got same value and that's why we captured the first element's value

        # Now we assign the value of first element to the last element
        arr[arrLen - 1] = first

        steps -= 1

    return arr


# Same logic is used here with first element being last element and last element being first element
def right_rotate(arr, steps):

    arrLen = len(arr)

    while steps > 0:
        first = arr[arrLen - 1]

        for j in range(arrLen - 1, 0, -1):
            arr[j] = arr[j - 1]

        arr[0] = first

        steps -= 1

    return arr


array = [28, 19, 64, 92, 57]
result = right_rotate(array, 3)
print(result)
