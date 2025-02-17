# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1]
        post_product = [1]
        hold = 1
        for i in range(len(nums)):
            pre_product.append(nums[i] * hold)
            hold *= nums[i]
        hold = 1
        for i in range(len(nums) - 1, -1, -1):
            post_product.insert(0, nums[i] * hold)
            hold *= nums[i]
        answer = []
        for i in range(len(nums)):
            answer.append(pre_product[i] * post_product[i + 1])
    
        return answer