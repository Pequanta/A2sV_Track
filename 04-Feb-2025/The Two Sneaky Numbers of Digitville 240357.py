# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_numbers = Counter(nums)
        res = []
        for num in count_numbers:
            if count_numbers[num] > 1:
                res.append(num)
        return res