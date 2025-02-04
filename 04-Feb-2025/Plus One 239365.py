# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = 0
        i = len(digits) - 1
        while i >= 0:
            if i == len(digits) - 1:
                sum_cont = digits[i] + 1
            else:
                sum_cont = digits[i] + overflow
            digits[i] = sum_cont % 10
            overflow = sum_cont // 10
            i -= 1
        if overflow != 0:
            digits.insert(0, overflow)
        return digits

