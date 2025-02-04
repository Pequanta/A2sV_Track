# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            if goal[i:] + goal[:i] == s:
                return True
        return False