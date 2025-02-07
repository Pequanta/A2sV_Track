# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cont_nums = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] in cont_nums:
                count += 1
                cont_nums.remove(nums[i])
            else:
                cont_nums.add(nums[i])

        return [count, len(cont_nums)]