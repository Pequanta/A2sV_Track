# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zeros = 0
        result = float("-inf")
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            result = max(result, right - left + 1)
        if result > len(nums):
            return k
        return result
            