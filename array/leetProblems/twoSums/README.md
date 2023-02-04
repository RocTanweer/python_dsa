# Two Sums

You can find this problem [here](https://leetcode.com/problems/two-sum/)

## Method 1

Initially I nested two loop to compare each element with every other elements

One loop => N work

Since we're doing one loop for each elements

Hense, N\*\*2 work is done

Time Complexity is O(N\*\*2)

Space Complexity is O(1) since constant space is used

## Method 2

In this, I tried doing the same thing but in just one loop. One way to do this is to keep track of all the previous elements. So we're using extra space to decrease runtime.

For each element, we'll check if their complimentary (target - nums[i]) exists in an array(history). If not, then we simply story the current element in it and move forward. If yes, then we return the index of the current element and index of that stored element in the original array (nums)

Since only N work is done, Time Complexity is O(N)

But we're using extra space to store the previous elements which increases linearly with the size of input(N), So, Space Complexity is O(N)
