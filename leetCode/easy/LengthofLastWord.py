class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s == '':
        #     return 0
        c = s.split(' ')
        b = []
        for i in c:
            if i != '':
                b.append(i)
        if len(b) > 0:
            return len(b[-1])
        else:
            return 0

if __name__ == '__main__':
    s = ""
    c = s.split(' ')
    # print(c[-1])
    so = Solution()
    l = so.lengthOfLastWord(s)
    print(l)