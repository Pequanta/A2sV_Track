# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurance_frequency = Counter(s)
        count = 0
        first_count = -1
        for letter in occurance_frequency:
            if count == 0:
                first_count = occurance_frequency[letter]
                count += 1
            else:
                if occurance_frequency[letter] != first_count:
                    return False
        return True