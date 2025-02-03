# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cont_prev = {}
        for i in range(len(nums)):
            if target - nums[i] in cont_prev:
                return [cont_prev[target- nums[i]], i]
            else:
                cont_prev[nums[i]] = i
