class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if 0x00 == len(s):
            return 0x00
        length = 0x00
        flag   = False
        for c in s[::-1]:
            if ' ' == c:
                if True == flag:
                    break
                continue
            length += 1
            flag = True
        return length

if __name__ == '__main__':
    p = Solution()
    print p.lengthOfLastWord('11 111   ')
    print p.lengthOfLastWord('11 ')
