# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        window_size = 1
        count_frequency = Counter(s[0])
        left = 0

        max_val = 1
        while left + window_size < len(s):
            count_frequency[s[left + window_size]] += 1
            if len(count_frequency) <= max_val:
                count_frequency[s[left]] -= 1
                if count_frequency[s[left]] == 0:
                    count_frequency.pop(s[left])
                left += 1
            else:
                window_size += 1
                max_val = max(max_val, window_size)

        return max_val
        