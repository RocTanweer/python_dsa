# Insertion Algorithm

This is one of the many array sorting algorithm

The main idea behind this algorithm is that the first element of any array is actually sorted

## Working

- Start with 2nd element as current element(since slice containing 1st element is sorted)
- Store the current element in a variable
- Start a reverse loop starting from previous index
- The loop will continue as long as index >= 0 and value at previous index > stored current value
- Override the value at current index by previous value
- After loop terminates, that's where we **insert** the stored current value

Time Complexity for worst case: O(N\*\*2)
Space Complexity for worst case: O(1)
