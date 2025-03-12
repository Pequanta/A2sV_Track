# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper_fn(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n % 2 == 0:
                half =  helper_fn(x, n // 2)
                return half * half
            return x* helper_fn(x, n - 1)
        if n >= 0:
            return helper_fn(x, n)
        return 1/helper_fn(x, -n)
        
        