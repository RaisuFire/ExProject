class Solution:
    pass
    # def numJewelsInStones(self, J, S):
        # n = 0
        # for j in J:
        #     for s in S:
        #         if j == s:
        #             n += 1
        # return n
        # print(n)

    # def numJewelsInStones(self, J, S):
    #     count = 0
    #     jewels = {}
    #     for char in J:
    #         if char not in jewels:
    #             jewels[str(char)] = 0
    #     for char in S:
    #         if char in jewels:
    #             count += 1
    #     return count


if __name__ == "__main__":
    # J = "aA"
    # S = "aAAbbbb"
    # so = Solution()
    # c = so.numJewelsInStones(J, S)
    # print(c)

    c = {"a": 0, "b": 0}
    print('a' in c)