def insertion_sort(arr):

    for i in range(0, len(arr) - 1):
        if arr[i + 1] < arr[i]:  # If the next element is less than current element, do this
            # Operate on the slice of array from beginning upto and including currnet element
            for j in range(0, i + 1):
                # Find index of the first element which is greater than element next to current element
                if arr[j] > arr[i + 1]:
                    # when found, insert element next to current element at that index while shifting all the array element to the right
                    arr.insert(j, arr[i + 1])
                    # The element we inserted is now located at one index to the right from it's original index, remove it from array
                    del arr[i + 2]
                    j = i - 1  # terminate the iteration, since insertion is done

        # else move forward

    return arr


array = [23, 64, 72, 15]
result = insertion_sort(array)
print(result)
