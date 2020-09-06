

#Time Complexity: O(N^2)  --> Due to arthemtic series, n-k + n-k+1 + n-k+2 +... + n-2 + n-1 +n  = N(n+1)/2 this O(n^2)
# Space Complexity: O(n) --> Space requried for the problem at worst case, scales linearlly with the problem size




def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
        return []

    ans = []
    nums.sort()
    for i in range(len(nums) - 2):

        left = i + 1
        right = len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:

            if nums[i] + nums[left] + nums[right] == 0:

                ans.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left = left + 1
                while left < right and nums[right] == nums[right - 1]:
                    right = right - 1

                left = left + 1
                right = right - 1

            elif nums[i] + nums[left] + nums[right] < 0:
                left = left + 1
            else:
                right = right - 1

    return ans
