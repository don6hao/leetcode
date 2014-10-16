
s = "   the    sky is    blue    "

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        plist = filter(lambda x: x, s.split(' '))
        plist.reverse()
        return ' '.join(plist)

p = Solution()
print p.reverseWords(s)
