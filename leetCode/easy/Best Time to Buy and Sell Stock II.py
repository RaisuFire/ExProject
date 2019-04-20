class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        d = 0
        c = []
        for i in range(len(prices)):
            if i < len(prices) -1 and prices[i] < prices[i+1]:
                c.append(prices[i+1]-prices[i])
                d += prices[i+1]-prices[i]
        print(d)
        return c


if __name__ == "__main__":
    input = [7, 1, 5, 3, 6, 4]
    so = Solution()
    c = so.maxProfit(input)
    print(c)
