class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ans = []
        # sa = set(A.split())
        # sb = set(B.split())
        #
        # for i in sa:
        #     if i not in sb:
        #         ans.append(i)
        # for i in sb:
        #     if i not in sa:
        #         ans.append(i)

        a = A.split()
        b = B.split()
        ss = set(a + b)
        dans = {}
        for i in ss:
            dans[i] = 0
        for i in a:
            dans[i] += 1
        for i in b:
            dans[i] += 1
        for k, v in dans.items():
            if v == 1:
                ans.append(k)
        return ans

if __name__ == "__main__":
    A = "apple apple"
    B = "banana"
    so = Solution()
    a = so.uncommonFromSentences(A, B)
    print(a)

