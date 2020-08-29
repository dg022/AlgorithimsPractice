
# Brute force solution

# Time Complexity: O(n^2), since every pair of digits is being checked, this scales quadraitcally as the size of the problem increases

# Space Complxity: O(1), since no external data strucutre is used for this aglorithim, space required is constant.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
    return []

# HashTable Solution

# Time Complexity: O(n): Linear Search through the nums list, scales linearally for each additonal increase to the problem size
#  Space Complexity: O(n-1): HashTable, at its worst case will store every value from nums in the table, until reaching the very last elemnt, as solution is guranteed O(n)

 def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashTable ={}
        for i in range(len(nums)):
            if target - nums[i] in HashTable:
                return [i, HashTable[target-nums[i]]]
            else:
                HashTable[nums[i]] = i
        return []
