class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = "aeiou"
        n = []
        for i in range(len(s)):
            if s[i] in res:
                n.append(i)

        def reverse_list(n):
            l = len(n)
            i = 0
            while i < l // 2:
                a = n[i]
                n[i] = i
                n[-i] = a
                i += 1

if __name__ == "__main__":
    # s = "leetcode"
    # so = Solution()
    # c = so.reverseVowels(s)

    n = [0, 1, 2, 5, 7]
    def reverse_list(n):
        l = len(n)
        i = 0
        while i < l // 2:
            a = n[i]
            n[i] = i
            n[-i] = a
            i += 1
        return n
    a = reverse_list(n)
    print(a)
