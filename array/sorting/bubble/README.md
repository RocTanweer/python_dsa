# Bubble Sort Algorithm

This is one of the sorting algorithm of array data structure.
The reason it is called bubble is because it bubbles out the larger/smaller elements to one side eventually sorting the array.

It swaps adjacent elements if they are not in order. In worst case, the smallest element lies in the right most side(in case of sorting in ascending order)
has to be swapped N to get to the left most side.
For 1 swap of N elements, N work is done. Hence, for N swap of N elements, N**2 work is done.
So, Time complexity is O(N**2)

Since contant amount of space is used throughout the algorithm, Space Complexity is O(1)
