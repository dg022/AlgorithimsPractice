
# Space Complexity: O(2n) --> O(n): I'm using two dicitonaries to store the occurences of each lettetr, for each additional letter, this resutls in a 1 for 1
# increase in space required to store it, therefore the space required scales linearlly with the respect to n.

#Time Complexity: O(2n) --> O(n): Iterate over the letters twice, for each addiontal letter, thsi results in 2 more  runs of the for loops. Since loops are O(1) in a
# dictionalry, the time required for this problem scales linearlly with respect to n.

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    Tdict = {}
    Sdict = {}

    for i in range(len(t)):

        if t[i] not in Tdict:
            Tdict[t[i]] = 0

        if t[i] in Tdict:
            Tdict[t[i]] = Tdict[t[i]] + 1

        if s[i] not in Sdict:
            Sdict[s[i]] = 0

        if s[i] in Sdict:
            Sdict[s[i]] = Sdict[s[i]] + 1

    for letters in Tdict:

        if letters not in Sdict:
            return False

        if Tdict[letters] != Sdict[letters]:
            return False
    return True
