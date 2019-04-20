class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i - 1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits



if __name__ == "__main__":
    n = [1,2,3]
    so = Solution()
    c = so.plusOne(n)
    print(c)

