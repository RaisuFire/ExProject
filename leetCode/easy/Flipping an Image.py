class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        def reversed_list(a):
            for i in range(len(a)):
                c = a.pop()
                a.insert(i, c)
            return a

        def invert(a):
            if a == 1:
                return 0
            else:
                return 1

        for i in A:
            reversed_list(i)
            for j in range(len(i)):
                i[j] = invert(i[j])
        return A


if __name__ == "__main__":
    a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    so = Solution()
    c = so.flipAndInvertImage(a)
    print(c)
"""
for row in A:
            for i in range((len(row)+1)/2):
                row[i], row[~i] = 1-row[~i], 1-row[i]
                
        return A
"""