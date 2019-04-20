class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        fir = 'qwertyuiopQWERTYUIOP'
        sec = 'asdfghjklASDFGHJKL'
        tth = 'zxcvbnmZXCVBNM'
        nwords = []

        def samerow(word, row):
            n = 0
            for i in word:
                if i not in row:
                    break
                n += 1
            if n == len(word):
                return nwords.append(word)

        for word in words:
            if word[0] in fir:
                samerow(word, fir)
            elif word[0] in sec:
                samerow(word, sec)
            elif word[0] in tth:
                samerow(word, tth)
            else:
                pass
        return nwords

if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    so = Solution()
    outwords = so.findWords(words)
    print(outwords)
