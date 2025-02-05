# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cont_word_counters = {}
        for word in strs:
            temp_word =  "".join(sorted(word))
            if temp_word in cont_word_counters:
                cont_word_counters[temp_word].append(word)
            else:
                cont_word_counters[temp_word] = [word]
        result = []
        for word in cont_word_counters:
            result.append(cont_word_counters[word])
        return result