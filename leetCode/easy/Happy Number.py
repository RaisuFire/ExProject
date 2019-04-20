class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_num(n):
            c = str(n)
            n = 0
            for i in c:
                n += int(i)**2
            return n
        if n == 1 or n == 7 or n == 10:
            return True
        while n > 10:
            n = next_num(n)
            if n == 1 or n == 7 or n == 10:
                return True
        return False

if __name__ == "__main__":
    s = 7
    so = Solution()
    c = so.isHappy(s)
    print(c)
