class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # idea: 25525511135 -> ["255.255.11.135", "255.255.111.35"]
        # because, number should be in [0, 255] so:
        # 25.525.511.135 is impossible for example. So it's impossible
        # as soon as there is a number > 255. Hence the algorithm resumes
        # to backtracking: Example (starting from the end)
        # 25525511135:
        # 5 < 255 -> 2552551113.5
        # 3 < 255 -> 255255111.3.5
        # ...
        # 25525511.1.3.5 but 25525511 > 255 so WRONG
        # so the idea is to put 4 dots, as soon as a number > 255, stop
        # the current branch of recursion
        res = []
        self.getIp(s, res, "", 4)
        return res
    
    def getIp(self, s, res, combi, nbDot):
        if nbDot == 0:
            if s == "":
                res.append(combi[:-1]) # to avoid last '.'
            return
        
        for i in range(3):
            num = s[:i+1]
            if i >= len(s):
                continue # to avoid duplicate
            if num and len(num) >= 2 and num[0] == "0":
                continue # to avoid number starting with 0
            if num and int(num) <= 255:
                self.getIp(s[i+1:], res, combi + num + ".", nbDot-1)