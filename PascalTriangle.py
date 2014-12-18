
INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution:
    def check_overflow(self, x):
        if x > INT_MAX or x < INT_MIN:
            return False
        return True
    def draw_line(self, line):
        tmplist = []
        pre_value = 0
        for i in line:
            tmplist.append(i+pre_value)
            pre_value = i
        tmplist.append(1)
        return tmplist

    # @return a list of lists of integers
    def generate(self, numRows):
        if 0x00 == numRows or False == self.check_overflow(numRows):
            return []
        rowlist = [[1]]
        for i in range(numRows-1):
            rowlist.append(self.draw_line(rowlist[i]))
        return rowlist


if __name__ == '__main__':
    p = Solution()
    print p.generate(0)
