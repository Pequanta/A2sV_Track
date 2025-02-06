# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count_zeros = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] == 0:
                count_zeros += 1
        result = [0] * len(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                result[index] = nums[i]
                index += 1
        return result
