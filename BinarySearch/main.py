from tests import tests


def test_location(arr, query, mid):
    '''It tells if the middle element is the query element or if the query element is in the left or right half of the array'''
    mid_number = arr[mid]

    if mid_number == query:
        if mid - 1 >= 0 and arr[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number > query:
        return 'left'
    else:
        return 'right'


def binary_search(arr, query):
    first_index, last_index = 0, len(arr) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2

        query_location = test_location(arr, query, mid_index)

        if query_location == 'found':
            return mid_index
        elif query_location == 'left':
            last_index = mid_index - 1
        elif query_location == 'right':
            first_index = mid_index + 1
    return -1


for test in tests:
    result = binary_search(**test["inputs"])
    print(result == test["output"])
