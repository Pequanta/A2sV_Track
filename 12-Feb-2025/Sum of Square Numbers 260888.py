# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, math.floor(math.sqrt(c)) + 1
        while a <= b:
            if a**2 + b**2 < c:
                a += 1
            elif a**2 + b**2 > c:
                b -= 1
            else:
                return True
        return False

