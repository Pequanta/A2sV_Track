# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        last_index = len(piles) // 3
        for i  in range(len(piles) - 2, last_index - 1, -2):
            result += piles[i]
        return result
        