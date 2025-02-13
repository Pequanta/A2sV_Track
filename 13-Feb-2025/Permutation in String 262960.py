# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        count_s1 = Counter(s1)
        count_s2 = Counter()

        window_size = len(s1)

        for i in range(len(s1)):
            count_s2[s2[i]] += 1
        
        if count_s2 == count_s1:
            return True


        left = 0
        for right in range(window_size, len(s2)):
            count_s2[s2[right]] += 1
            count_s2[s2[left]] -= 1
            if count_s2 == count_s1:
                return True

            left += 1
        return False
