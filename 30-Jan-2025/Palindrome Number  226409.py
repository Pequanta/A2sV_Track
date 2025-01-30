# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        size = 0
        num1 = x
        while num1 > 0:
            size += 1
            num1 //= 10
        num2 = 0
        num3 = x
        while num3 > 0:
            num2 += (num3 % 10) * (10**(size - 1))
            size -= 1
            num3 //= 10
        return num2 == x