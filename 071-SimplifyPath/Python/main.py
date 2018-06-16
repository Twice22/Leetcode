class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        folders = path.split("/")
        mypath = []
        for folder in folders:
            if folder == "" or folder == ".":
                continue
            if folder != "..":
                mypath.append(folder)
            elif mypath:
                del mypath[-1]

        return "/" + "/".join(mypath)