# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cont_count = Counter({0:1})

        prefix_sum = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            result += cont_count[prefix_sum - goal]
            cont_count[prefix_sum] += 1
        return result