# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random as rand
class RandomizedSet:

    def __init__(self):
        self.lst = []        

    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.lst:
            self.lst.remove(val)
            return True
        return False
    def getRandom(self) -> int:
        rand_element_index = rand.randrange(0,len(self.lst))
        return self.lst[rand_element_index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()