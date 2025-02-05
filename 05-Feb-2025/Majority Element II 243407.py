# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cont_counter = Counter(nums)
        check_number = len(nums) // 3
        res = []
        for num in cont_counter:
            if cont_counter[num] > check_number:
                res.append(num)
        return res