class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        elif numRows == 1:
            return s
        
        result = ""
        size = len(s)
        modulo = (2 * (numRows - 1))
        
        # initialization
        idx = [i for i in range(size) if i % modulo == 0]
        queue = [(idx[i], idx[i+1]) for i in range(len(idx) - 1)]
        
        # add last tuple if exists
        if idx[-1] < size:
            queue.append((idx[-1], idx[-1]+modulo))
        
        visited = {i: False for i in range(size)}
        
        while queue:
            new_queue = []
            beg, end = -1, -1
            for idx in queue:
                beg, end = idx
                if beg < size and not visited[beg]:
                    result += s[beg]
                    visited[beg] = True
                if end < size and not visited[end]:
                    result += s[end]
                    visited[end] = True
                if beg <= end:
                    new_queue.append((beg+1, end-1))
            
            queue, new_queue = new_queue, []
            
        return result
        