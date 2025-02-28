# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        max_prefix = float("-inf")
        for i in range(len(nums)):
            prefix += nums[i]
            max_prefix = max(prefix, max_prefix)
            if prefix < 0:
                prefix = 0
        min_prefix = float("inf")
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            min_prefix = min(min_prefix, prefix)
            if prefix > 0:
                prefix = 0
        return max(max_prefix, abs(min_prefix))
