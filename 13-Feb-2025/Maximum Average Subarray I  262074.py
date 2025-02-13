# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum = 0
        for i in range(k):
            total_sum += nums[i]
        max_sum = total_sum

        for right in range(k , len(nums)):
            total_sum -= nums[right - k]
            total_sum += nums[right]
            max_sum = max(max_sum , total_sum)
        return max_sum / k