class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n).split('b')[1]
        if len(s) <= 1:
            return True
        if s[0] == s[1]:
            return False
        for i in range(0, len(s), 2):
            if s[i] != s[0]:
                return False
        for i in range(1, len(s), 2):
            if s[i] != s[1]:
                return False
        return True


if __name__ == "__main__":
    n = 5
    so = Solution()
    print(so.hasAlternatingBits(n))

    """
    last = ''
        while True:
            if 0 == n:
                break
            cur = 0
            temp = n
            n >>= 1
            if (n << 1)< temp:
                cur = 1
            if '' == last:
                last = cur
                continue
            if cur == last:
                return False
            last = cur
        return True
    """