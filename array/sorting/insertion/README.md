# Insertion Algorithm

This is one of the many array sorting algorithm

The main idea behind this algorithm is that the first element of any array is actually sorted

## Working

Let's take arr = [a, b, c, d, e] as example

I will explain the operation included in the first iteration.

- Assume the slice of original array containing first element (arr[0, 1]) is sorted
- Compare the last element of sorted slice (a) with the first element of unsorted slice (b)
- If b is less than a, take the sorted slice and find the index of first occuring element which is greater than b and insert b at that index causing all the elements to shift one step to the right. Now delete that b which is now located at one index to the right from it's original index
- If the b is greater than the a, then don't do anything and move forward
- Do this for all the elements

Time Complexity for worst case: O(N\*\*2)
Space Complexity for worst case: O(1)
