# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n <= 1:
                return 1
            else:
                return n * (factorial(n - 1))
        cont = factorial(n)
        count = 0
        while cont % 10 == 0 and cont > 0:
            count += 1
            cont //= 10
        return count