# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sum_of_digit(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res
        temp_result = ""
        for i in range(len(s)):
            letter_index = ord(s[i]) - 96
            temp_result += str(letter_index)
        while k > 0:
            temp_result = str(sum_of_digit(int(temp_result)))
            k -= 1
        result = int(temp_result)
        return result