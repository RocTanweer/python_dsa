# Merge Sort Alogirithm (Array)

Working of this sorting algorithm:

- Get the original array as input
- If it's length is one, then array is said to be sorted so return it
- Otherwise, sort the left and right slice of the array
- create new empty array(or operate on the original one)
- compare left most elements of each sorted slice
- fill the new array in order or change element value of original array
- return the new array or the mutated array

Since for N inputs, we are doing N work (recursive calls) but log(N) times as
number of elements in each recursive call gets half.
So Time complexity for worst case is O(Nlog(N)).
Space Complexity is O(N) since each recursive function call is taking space and that increases linearly with size of input N
