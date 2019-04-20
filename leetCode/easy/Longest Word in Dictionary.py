class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        my_dict = set(words)
        words.sort()
        words.sort(key=lambda x: len(x), reverse=True)

        for word in words:
            w = word
            print("debug**1",w, word)
            while w in my_dict:
                print("debug", w, word)
                w = w[:-1]
            print("debug close", w, word)
            print("+++++++++++++++++++++++++++++++")
            if not w:
                print("final", w, word)
                return word
        return ""

        # wdic = {}
        # for i in range(len(words)):
        #     n = 0
        #     for word in words:
        #         if word in words[i]:
        #             n += 1
        #     wdic[words[i]] = n
        # print(wdic)
        # n = 0
        # w = []
        # for v in wdic.values():
        #     if n < v:
        #         n = v
        # for k, v in wdic.items():
        #     if v == n:
        #         w.append(k)
        # print(w)
        # return sorted(w)[0]


if __name__ == '__main__':
    words = ["m", "mo", "moch", "mocha", "l", "lat", "latt", "latte", "c", "ca", "cat"]
    so = Solution()
    c = so.longestWord(words)
    print(c)
