# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")

        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            column = min(height[right], height[left])
            max_area = max(max_area, width * column)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_area