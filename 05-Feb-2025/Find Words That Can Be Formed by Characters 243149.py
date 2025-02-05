# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter_chars = Counter(chars)
        result = 0
        for word in words:
            get_count = Counter(word)
            flag = True
            for letter in get_count:
                if get_count[letter] > counter_chars[letter]:
                    flag = False
            if flag:
                result += len(word)
        return result