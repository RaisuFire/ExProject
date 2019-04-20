class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        dict_letter = {}
        upLetter = [chr(i) for i in range(65, 91)]
        l = len(upLetter)
        for i in range(l):
            dict_letter[i] = upLetter[i]
        while n / l > 0:
            i = (n-1) % l
            n = int((n-1) / l)
            ans = dict_letter[i] + ans
        return ans

        s = ''

        d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
             13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
             25: 'Z'}

        while n > 0:
            s += d[(n - 1) % 26]
            n = (n - 1) // 26

        return s[::-1]
    # print(dict_letter)
    # print([chr(i) for i in range(65, 91)])


if __name__ == '__main__':
    n = 1
    so = Solution()
    c = so.convertToTitle(n)
    print(c)
