# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[min_index] , nums[i] = nums[i], nums[min_index]
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result