# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_result = float("-inf")
        for right in range(len(nums)):
            prefix_sum += nums[right]

            max_result = max(prefix_sum, max_result)
            if prefix_sum < 0:
                prefix_sum = 0
        return max_result