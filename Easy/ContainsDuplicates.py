


# Brute Force

# Time Complexity: O(n^2): Checks every pair of integers in the list, this scales quadraitcally as the problem size grows
# Space Complexity: O(1): No external data structure is used, space stays the same regardless of problem size.


def containsDuplicate(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False


# Sorting Method


# Time Complexity: O(NLogN): Performs a python implemented sorting algorithim, which in worst case nlogn, then a single pass through to check for duplicates.
# Space Complexity: O(1): No external data structure is used, space stays the same regardless of problem size.
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# If in need of O(n) time and space complxity, consider hashtable approach.