# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        loosers = set()
        loosers_more_match = set()
        for match in matches:
            winners.add(match[0])
            if match[1] in loosers:
                loosers_more_match.add(match[1])
            loosers.add(match[1])
        return [sorted(list(winners - loosers)), sorted(list(loosers - loosers_more_match))]
