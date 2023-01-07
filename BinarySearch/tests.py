tests = [
    # When query is in the middle of the array
    {
        "inputs": {
            "arr": [1, 3, 6, 7, 19, 22, 53],
            "query": 7
        },
        "output": 3
    },
    # When query is the first element
    {
        "inputs": {
            "arr": [1, 3, 6, 7, 19, 22, 53],
            "query": 1
        },
        "output": 0
    },
    # When query is the last element
    {
        "inputs": {
            "arr": [1, 3, 6, 7, 19, 22, 53],
            "query": 53
        },
        "output": 6
    },
    # When query is not in the array
    {
        "inputs": {
            "arr": [1, 3, 6, 7, 19, 22, 53],
            "query": 43
        },
        "output": -1
    },
    # When the array is empty
    {
        "inputs": {
            "arr": [],
            "query": 32
        },
        "output": -1
    },
    # There is just one element in the array
    {
        "inputs": {
            "arr": [32],
            "query": 32
        },
        "output": 0
    },
    # The array contains repeating numbers
    {
        "inputs": {
            "arr": [1, 3, 6, 6, 6, 7, 19, 22, 22, 22, 22, 53, 53],
            "query": 3
        },
        "output": 1
    },
    # The query number is repeating in the array
    {
        "inputs": {
            "arr": [1, 3, 6, 7, 19, 22, 22, 22, 53],
            "query": 22
        },
        "output": 5
    }
]
