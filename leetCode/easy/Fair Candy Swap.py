class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # a = sum(A)
        # b = sum(B)
        # c = (a - b) / 2
        #
        # for i in A:
        #     if (i - c) in B:
        #         return [i, i-c]

        a = set(A)
        b = set(B)
        diff = (sum(A) - sum(B)) // 2
        for i in a:
            if (i - diff) in b:
                return [i, i - diff]


if __name__ == "__main__":
    # A = [1, 2, 5]
    # B = [2, 4]
    A = [1, 1]
    B = [2, 2]
    so = Solution()
    c = so.fairCandySwap(A, B)
    print(c)
