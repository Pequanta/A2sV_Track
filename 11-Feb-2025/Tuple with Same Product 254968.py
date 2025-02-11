# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hash_multiple = Counter()
        result = 0
        for i in range(len(nums)):
            for j in range(i):
                result += hash_multiple[nums[i] * nums[j]] * 8
                hash_multiple[nums[i] * nums[j]] += 1
        return result