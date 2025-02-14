# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count_ones = 0
        steps = 0
        for i in range(len(s)):
            if s[i] == "1":
                count_ones += 1
            else:
                steps += count_ones
        return steps
