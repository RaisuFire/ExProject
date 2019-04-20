class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[::-1]
        return ans

if __name__ == "__main__":
    s = "hello"
    so = Solution()
    c = so.reverseString(s)
    print(c)

"""
Python 简化太厉害了。。所以看一下Java的实现
public class Solution {
    public String reverseString(String s) {
        char[] word = s.toCharArray();
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            char temp = word[i];
            word[i] = word[j];
            word[j] = temp;
            i++;
            j--;
        }
        return new String(word);
    }
}
"""