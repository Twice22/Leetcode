class Solution    
    def firstUniqChar2(self, s)
        
        type s str
        rtype int
        
        visited = set()
        d = {}
        for i, letter in enumerate(s)
            if letter not in visited
                d[letter] = i
                visited.add(letter)
            elif letter in d
                del d[letter]
                
        return min(d.values()) if d else -1
    
    def firstUniqChar(self, s)
        # we might assume lowercase letters
        letters = azertyuiopqsdfghjklmwxcvbn
        return min( (s.index(l) for l in letters if s.count(l) == 1), default=-1)