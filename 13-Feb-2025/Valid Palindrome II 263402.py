# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        right = len(s) - 1
        left = 0
        flag_one = flag_two = True
        while left < right:
            if s[left] != s[right]:
                count += 1
                right -= 1
            else:
                left += 1
                right -= 1
            if count > 1:
                flag_one = False
        left = 0
        right = len(s)  - 1
        count = 0
        while left < right:
            if s[left] != s[right]:
                count += 1
                left += 1
            else:
                left += 1
                right -= 1
            if count > 1:
                flag_two = False
        

        return flag_one or flag_two