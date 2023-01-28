# Algorithm to reverse an array

This algorithm takes an array and reverse the order in which elements appear while mutating the original array.

This method basically swaps elements which are mirror image of one another. That is, 0th element is swapped with last element, 1st element with 2nd last and so on.

Since after coming at middle element, all the elements must be swapped with each other causing the array to be reversed. Hence, For array of N element, we iterate N//2 times

Time Complexity: O(N)

Space Complexity: O(1)
