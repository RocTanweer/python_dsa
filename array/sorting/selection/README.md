# Selection Sort Algorithm (Array)

This is one of the sorting algorithm of array data structure that uses a selection process to sort an array.

## Selection process:

- It divides the array in two parts (sorted and unsorted)
- Initially len(sorted) = 0 and len(unsorted) = len(array)
- It takes the first element of unsorted part (arr[0]) initially
- It, then, find the smallest in rest portion by comparing them with first element
- It, then, swap it with first element of the unsorted portion.
- Now, one traversal is complete.
- Currently, len(sorted) = 1 and len(unsorted) = len(array - 1)
- Now, it takes array from arr[1] to last element as the new unsorted part.
- first element = arr[1] and rest will be unsorted part
- The process goes on with new unsorted part.

Since for each N elements of array, N traversal is required and 1 traversing mean N work done.
So total work done is N**2.
Hence Time Complexity in worst case is O(N**2)
Space Complexity is O(1) since no new memory is allocated
