# Time Complexity O(n)
# Space Complexity O(1)
def sortArrayByParityII(self, A: List[int]) -> List[int]:
    j = 1

    for i in range(0, len(A), 2):

        # I will always be evenm we start at 0 and increment by two
        # If A[i] is odd, then we know its wrong, we need to find
        if A[i] % 2 != 0:

            # We look to find an even number, in an odd posotion
            # Since J starts at 1, and icnrements by 2, it will awlays be odd
            while A[j] % 2 != 0:
                j = j + 2

            # Now swap whatsa at i and j

            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    return A