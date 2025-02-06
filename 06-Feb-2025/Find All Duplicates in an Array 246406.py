# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cont_counter = Counter(nums)
        result = set()
        for i in range(len(nums)):
            if cont_counter[nums[i]] > 1:
                result.add(nums[i])
        return list(result)