class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        
        # if empty string
        if not s:
            return 0
        
        # nb position = size + number of
        # position between each letter = (N - 1) + 2
        nb_position = 2 * size + 1
        
        # initialize the array that will contain
        # the length of the biggest palindrom
        # in each position
        palindromes = [0] * nb_position
        
        # initialize the array with 2 first elements
        # that are known: in position 0 there is no
        # palindrom because we can't expend left or right
        # in position 1 we point on a letter and we can't
        # expand left so the length in position 1 is 1
        palindromes[0] = 0
        palindromes[1] = 1
        
        centerPosition = 1
        centerRightPosition = 2
        i = 0 # current position (right)
        i_conjugate = 0 # it's index = symmetric of i by the centerPosition
        
        maxLength = 1 # 1 because we discarded empty string
        maxCenterPosition = 1 # 1 because we discarded empty string
        
        start, end, diff = -1, -1, -1
        
        # start at 2 because we already fill in position 0 and 1
        for i in range(2, nb_position):
            # get symmetric left index of i by centerPosition
            i_conjuguate = 2 * centerPosition - i
            palindromes[i] = 0
            
            diff = centerRightPosition - i
            if diff > 0:
                # case 1 and case 2
                palindromes[i] = min(palindromes[i_conjuguate], diff)
            
            
            # try to expand palindrome in current position i
            # while there is still right space to expand the palindrome
            # AND there is still left space to expand the palindrome
            # AND ((if even number of positions => increment by 1 the length
            # of the palindrome because even number are pointers in between 2
            # letters) (if odd number of positions => increment by 1 only if
            # left and right characters match)
            try:
                while ((i + palindromes[i]) < nb_position \
                and (i - palindromes[i] > 0)) and \
                ( (i + palindromes[i] + 1) % 2 == 0 or \
                 s[(i + palindromes[i] + 1)//2] == s[(i - palindromes[i] - 1)//2]):
                    palindromes[i] += 1
            except Exception as e:
                 pass
                 
            # update the longest palindrome
            if palindromes[i] > maxLength:
                maxLength = palindromes[i]
                maxCenterPosition = i
            
            # update the next extreme right position
            # if current position i + lengthpalindrome[i]
            # becomes greater
            if i + palindromes[i] > centerRightPosition:
                centerPosition = i
                centerRightPosition = i + palindromes[i]
        
        beg = (maxCenterPosition - maxLength) // 2
        end = beg + maxLength
        
        return s[beg:end]
            
        
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        beg_idx = 0
        end_idx = 0
        
        size = len(s)-1
        max_len = 1
        
        
        for i, letter in enumerate(s):
            
            r_idx = l_idx = i
            
            # odd palindrome
            while 0 < l_idx and r_idx < size and s[l_idx-1] == s[r_idx+1]:
                l_idx -= 1
                r_idx += 1
            
            if r_idx - l_idx > end_idx - beg_idx:
                beg_idx, end_idx = l_idx, r_idx
                
            # even palindrome
            if i > 0 and s[i-1] == s[i]:
                r_idx, l_idx = i, i-1
                while 0 < l_idx and r_idx < size and s[l_idx-1] == s[r_idx+1]:
                    l_idx -= 1
                    r_idx += 1
                
                if r_idx - l_idx > end_idx - beg_idx:
                    beg_idx, end_idx = l_idx, r_idx 
                
        
        return s[beg_idx: end_idx+1]
            