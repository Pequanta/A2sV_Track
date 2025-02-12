# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        result = 0

        while left <= right:
            if people[right] >= limit:
                result += 1
                right -= 1
                continue
            total_weight = people[right] + people[left]
            if total_weight > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            result += 1
        return result