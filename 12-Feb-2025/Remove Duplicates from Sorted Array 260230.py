# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        count = 0
        while right < len(nums):
            if nums[right] != nums[left]:
                count += 1
                right += 1
                left = right - 1
            else:
                nums.remove(nums[right])
    