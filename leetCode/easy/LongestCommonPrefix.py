class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        if strs == []:
            return s
        strs = sorted(strs, key=lambda str: len(str))
        first = strs[0]
        for i in range(len(first)):
            c = 0
            for j in strs:
                if j[i] == first[i]:
                    c += 1
                else:
                    break
            if c == len(strs):
                s += first[i]
            else:
                break
        return s

if __name__ == "__main__":
    strs = ["aca","cba"]
    so = Solution()
    c = so.longestCommonPrefix(strs)
    print(c)


