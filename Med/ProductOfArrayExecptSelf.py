
# Space Complexity: O(3N) -> o(N): Three external arrays arrays used to store the output, the left and right multiplcaiton
# results as well. With each addtional incrase in the problem size, each array will increase in space usage by a linear amount.

# Time Complexity: O(3n) -> O(N): Three loops of the same size N, are iterated over, the time reauried to conduct these for loops linearlly scales with the problem size.


def productExceptSelf(self, nums: List[int]) -> List[int]:
    if len(nums) == 2:
        return [nums[1], nums[0]]

    left = []
    right = []
    output = []

    for i in range(len(nums)):
        if i == 0:
            left.append(1)
        elif i == 1:
            left.append(nums[0])
        else:
            left.append(nums[i - 1] * left[-1])

    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:

            right.append(1)
        elif i == len(nums) - 2:

            right.append(nums[-1])
        else:

            right.append(nums[i + 1] * right[-1])

    for i in range(len(nums)):
        output.append(left[i] * right[len(right) - 1 - i])

    return output