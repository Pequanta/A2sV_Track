# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comparator(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        nums = [str(nums[i]) for i in range(len(nums))]

        nums.sort(key = cmp_to_key(comparator))
        if nums[0] == "0":
            return "0"
        return "".join(nums)