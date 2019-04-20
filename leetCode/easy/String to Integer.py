class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        lower_bound = -2 ** 31
        upper_bound = 2 ** 31 - 1
        nums = str.split()
        if not nums:
            return 0
        tmp = ""
        avai = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        flag = False
        for i, c in enumerate(nums[0]):
            if i == 0:
                if c in avai or c == '-' or c == '+':
                    tmp += c
                else:
                    break
            else:
                if c in avai:
                    tmp += c
                else:
                    break
        try:
            num = int(tmp)
        except:
            return 0
        if num < lower_bound: return lower_bound
        if num > upper_bound: return upper_bound
        return num


    #         str = str.strip()
    #         i = 0
    #         while i <= len(str)-1:
    #             if str[0] == '-' or str[0] == '+':
    #                 i += 1
    #             elif is_number(str[i]):
    #                 i += 1
    #             else:
    #                 break
    #         if i == 0:
    #             return 0
    #         str = str[:i]
    #         ans = int(str)
    #         if ans > 2 ** 31:
    #             ans = 2 ** 31
    #         if ans < -2 ** 31:
    #             ans = - 2** 31
    #         return ans


    def test(self):
        str = "42"
        str1 = "   -42"
        str2 = "4193 with words"
        str3 = "words and 987"
        str4 = "-91283472332"
        strl = []
        strl.append(str)
        strl.append(str1)
        strl.append(str2)
        strl.append(str3)
        strl.append(str4)

        for i in strl:
            print(self.myAtoi(i))


#
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False


if __name__ == "__main__":
    str = '42'
    so = Solution()
    c = so.test()
    print(c)
