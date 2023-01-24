# Sentinel Linear Search (Array)

This algorithm is quite similar to Linear Search Algorithm. The only difference is that it reduces the number of comparison significantly.

Linear Search Algorithm make comparison for both 'query element with each array element' and also 'current index with the last index of array' to prevent 'indexoutofbound exception'
Given N elements in array, it will make around 2N comparisons.

Sentinel Linear Search Algorithm avoid comparison for index.
Given N elements in array, it will make N + 2 comparisons.
