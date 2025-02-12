# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        i = 0
        hold = 0
        while i < len(costs) and hold <= coins:
            hold += costs[i]
            if hold <= coins:
                result += 1
            i += 1
        return result