
#Time Complexity: o(N) single pass over string
# Space Complexity: O(N): Stack grows linearlly with size of string input

def complement(s1: str, s2: str) -> bool:
    if s1 == "(":
        if s2 == ")":
            return True
        else:
            return False

    if s1 == "{":
        if s2 == "}":
            return True
        else:
            return False

    if s1 == "[":
        if s2 == "]":
            return True
        else:
            return False

    return False


class Solution:

    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        for i in range(len(s)):

            if not stack or not complement(stack[-1], s[i]):
                stack.append(s[i])

            else:
                stack.pop()

        if not stack:
            return True

        return False




