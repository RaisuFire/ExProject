class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverstr(s):
            a = ''
            while s:
                a += s[-1]
                s = s[:-1]
            return a

        ans = ''
        s_list = s.split()
        for i in s_list:
            s = reverstr(i)
            ans += s + " "
        return ans[:-1]
"""
总是忘记 join
        l = s.split(' ')
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return ' '.join(l)

"""

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    so = Solution()
    c = so.reverseWords(s)
    print(c)
