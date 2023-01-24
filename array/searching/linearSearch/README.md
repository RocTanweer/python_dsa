# Linear Search Algorithm (Array)

This algorithm is designed to search or check for a value in an array by going through each of it's element sequentially

As the number of element increases, the time it takes to go through them increases linearly. Hence time complexity is O(n)
It takes constant amount of space, So it's space complexity is O(1)

In each iteration, it is making two comparison(comparing query value and array's element, comparing current index with array's last index to prevent 'indexoutofbound exception')

Number of comparison can be reduced by using another linear search algorithm known as 'Sentinel Linear Search'
