class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits), -1, -1):
            if digits is None:
                return
            elif digits[i] == 9:
                digits[i-1] += 1
                digits[i] = 0
            else:
                digits[i] += 1

        # i = -1
        # ditlen = len(digits)
        # if digits is None:
        #     return
        # elif digits[i] != 9:
        #     digits[i] += 1
        #     if ditlen <= len(digits):
        #         return digits
        #     else:
        #         for i in range(len(digits), 1):
        #             digits.append(0)
        #         return digits
        # else:
        #     digits[i] = 0
        #     return self.plusOne(digits[:-1])


if __name__ == "__main__":
    digits = [1, 2, 9]
    so = Solution()
    x = so.plusOne(digits)
    print(x)