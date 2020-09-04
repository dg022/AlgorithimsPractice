

# Time Complexity: O(n) Single Pass over the input arrary, therefore the time required scales lineally with the problem size.

# Space Complexity: O(N), one extenral array is used to track the current largest sum, scales linearlly with the problem size.


def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    summer = []
    summer.append(nums[0])

    for i in range(1, len(nums)):
        if nums[i] > summer[-1] and nums[i] + summer[-1] < nums[i]:

            summer.append(nums[i])
        else:
            summer.append(summer[-1] + nums[i])

    return max(summer)