# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        for letter in count_s:
            if letter not in count_t:
                return False
            count_t[letter] -= count_s[letter]
        for letter in count_t:
            if count_t[letter] != 0:
                return False

        return True