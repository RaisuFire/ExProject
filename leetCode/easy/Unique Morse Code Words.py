class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        A = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a = [chr(i) for i in range(97, 123)]
        dictA = {}
        for i in range(len(a)):
            dictA[a[i]] = A[i]

        mrlist = []
        for word in words:
            s = ''
            for c in word:
                s += dictA[c]
            mrlist.append(s)
        ans = len(set(mrlist))
        return ans


if __name__ == "__main__":
    A = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    a = [chr(i) for i in range(97, 123)]
    dictA = {}
    for i in range(len(a)):
        dictA[a[i]] = A[i]
    words = ["gin", "zen", "gig", "msg"]
    so = Solution()
    c = so.uniqueMorseRepresentations(words)
    print(c)

