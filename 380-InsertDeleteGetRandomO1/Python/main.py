import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.arr = []
        self.size = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val] = self.size
            self.arr.append(val)
            self.size += 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            idx = self.d[val]
            del self.d[val]
            if self.arr[-1] != val:
                self.d[self.arr[-1]] = idx
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            del self.arr[-1]
            self.size -= 1
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.size-1)
        return self.arr[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()