import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.sub(r'[!?\',;.]', '', paragraph).lower().split()
        words = []
        for p in paragraph:
            if p not in banned:
                words.append(p)
        c = []
        for i in range(len(words)):
            n = 0
            for word in words:
                if words[i] == word:
                    n += 1
            c.append(n)
        d = sorted(c)
        for i in range(len(c)):
            if d[-1] == c[i]:
                return words[i]


'''
solutation in discuss 
It's better than my so cause It use dict

        table = set(string.punctuation)
        para = "".join([ch for ch in paragraph.lower() if ch not in table])
        words = para.split()
        d = {}
        for w in words:
            if w in banned:
                continue
            if w in d:
                d[w]+=1
            else:
                d[w] = 1
        
        maxx = 0
        key = ""
        for k,v in d.items():
            if v>maxx:
                maxx = v
                key = k
        return key
'''

if __name__ == "__main__":
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # paragraph = 'air.'
    # banned = []
    paragraph = "abc abc? abcd the jeff!"
    banned = ["abc","abcd","jeff"]
    so = Solution()
    d = so.mostCommonWord(paragraph, banned)
    print(d)
