class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0

        count = -1
        rec1 = 0
        rec2 = 0
        prev_digit = None
        for digit in s:
            print("rec1", rec1, "rec2", rec2)
            if prev_digit == digit:
                rec1 += 1
                if rec2 >= rec1:
                    count += 1
            else:
                rec2 = rec1
                rec1 = 1
                count += 1
            prev_digit = digit
        return count


if __name__ == '__main__':
    s = '00110011'
    so = Solution()
    c = so.countBinarySubstrings(s)
    print(c)

    """
    0011", "01", "1100", "10", "0011", and "01".
    """
