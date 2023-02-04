def two_sums_o2(nums, target):
    '''
        Time: O(n**2), Space: O(1)
    '''

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]


def two_sums_o1(nums, target):
    '''
        Time: O(N), Space: O(N)
    '''

    history = []

    for i in range(len(nums)):

        if (target - nums[i]) not in history:
            history.append(nums[i])
        else:
            return [i, history.index(target - nums[i])]
