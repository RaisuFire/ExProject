class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        def divinum(num):
            n = num
            while n > 0:
                r = n % 10
                n = n // 10
                if r == 0:
                    break
                if num % r != 0:
                    return False
            return True

        for i in range(left ,right+1):
            if divinum(i) == True:
                nums.append(i)
        return nums


if __name__ == '__main__':
    # left = 1
    # right = 22
    # so = Solution()
    # c = so.selfDividingNumbers(left, right)
    # print(c)



    def divinum(num):
        n = num
        while n > 0:
            r = n % 10
            n = n // 10
            if r == 0:
                break
            if num % r != 0:
                return False
        return True
    print(divinum(10))