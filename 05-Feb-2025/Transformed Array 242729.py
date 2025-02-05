# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        length = len(nums)
        for i in range(len(nums)):
            result[i] = nums[(i + nums[i])%length]
        return result
