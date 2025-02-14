# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = Counter()
        
        left = 0

        result = float("-inf")
        for right in range(len(fruits)):
            fruit_types[fruits[right]] += 1

            while len(fruit_types) > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    fruit_types.pop(fruits[left])
                left += 1
            result = max(result , right - left + 1)
        return result