# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        count_s = Counter()

        if len(p) > len(s):
            return []
        window_size = len(p)

        for i in range(window_size):
            count_s[s[i]] += 1
        k = window_size
        result = []
        if count_s == count_p:
            result.append(0)
        left = 0
        for right in range(k , len(s)):
            count_s[s[left]] -= 1
            count_s[s[right]] += 1
            if count_s[s[left]] == 0:
                count_s.pop(s[left])
            if count_s == count_p:
                result.append(left + 1)
            left += 1
        return result




        
        