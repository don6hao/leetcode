sss = "A man, a plan, a canal: Panama"
ssss = "race a car"
sssss = ""
import re
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if None == s:
            return True
        ss = (re.sub("[^A-Za-z0-9]*", "", s)).upper()
        low = 0x00
        high = len(ss) - 1
        while low < high:
            if ss[low] != ss[high]:
                return False
            low  += 1
            high -= 1
        return True

p = Solution()
print p.isPalindrome(sssss)
