# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def separate(num):
            res = []
            while num > 0:
                res.append(num % 10)
                num //= 10
            return res[::-1]
        result = []
        for num in nums:
            if num >= 10:
                result.extend(separate(num))
            else:
                result.append(num)
        return result
        