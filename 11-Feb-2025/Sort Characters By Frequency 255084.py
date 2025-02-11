# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        cont_count = Counter(s)
        s = list(set(s))
        for i in range(len(s)):
            for j in range(1, len(s) - i):
                if cont_count[s[j]] > cont_count[s[j - 1]]:
                    s[j], s[j - 1] = s[j - 1], s[j]

        result = []
        for i in range(len(s)):
            result.append(s[i] * cont_count[s[i]])
        return "".join(result)
