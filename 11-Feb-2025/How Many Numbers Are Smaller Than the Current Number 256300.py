# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            check = nums[i]
            count = 0
     
            for j in range(len(nums)):
                if nums[j] < check:
                    count += 1
            res.append(count)
        return res
                