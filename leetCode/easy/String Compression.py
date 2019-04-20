class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        c = sorted(list(set(chars)))
        ansd = {}
        for i in c:
            ansd[i] = 0

        for i in chars:
            ansd[i] += 1
        a = ''
        for k, v in ansd.items():
            a += k
            if v == 0:
                continue
            a += str(v)
        b = []
        for i in a:
            b.append(i)
        return len(b)

if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    so = Solution()
    a = so.compress(chars)
    print(a)
