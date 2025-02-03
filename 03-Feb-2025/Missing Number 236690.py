# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        cont_set = set(range(length + 1))
        for num in nums:
            cont_set.remove(num)
        return cont_set.pop()
        