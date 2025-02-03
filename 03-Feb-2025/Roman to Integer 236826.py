# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution(object):
    def romanToInt(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sym  = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result  = 0
        while i < len(s):
            if i > 0 and sym[s[i - 1]] < sym[s[i]]:
                result -= sym[s[i-1]]
                result += sym[s[i]] - sym[s[i-1]]
            else:
                result += sym[s[i]]
            i += 1

        return result