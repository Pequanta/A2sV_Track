# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        right = len(skill) - 1
        result = 0
        prev_sum = -1
        for left in range(len(skill) // 2):
            if prev_sum != -1 and skill[left] + skill[right] != prev_sum:
                return -1
            result += skill[left] * skill[right]
            prev_sum = skill[left] + skill[right]
            right -= 1
        return result
        