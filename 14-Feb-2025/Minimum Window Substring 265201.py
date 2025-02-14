# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_window = defaultdict(int)

        count_t = Counter(t)

        acquired = 0
        required = len(count_t)

        n = len(s)

        left = 0

        solution = [-1, n + 1]
        for right in range(n):
            freq_window[s[right]] += 1

            if freq_window[s[right]] == count_t[s[right]]:
                acquired += 1 
            while acquired == required:
                if solution[1] - solution[0] > right - left:
                    solution[0], solution[1] = left, right
                freq_window[s[left]] -= 1
                if freq_window[s[left]] < count_t[s[left]]:
                    acquired -= 1
                left += 1

        if solution[1] - solution[0] >= n:
            return ""
        else:
            return s[solution[0]: solution[1] + 1]
        
