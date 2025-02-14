# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_(left ,right):
            while left < right:
                nums[right] , nums[left] = nums[left], nums[right]
                right -= 1
                left += 1
        k = k % len(nums)
        reverse_(0 , len(nums) - 1)
        reverse_(0, k - 1)
        reverse_(k, len(nums) - 1)


        

        
        