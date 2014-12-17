#!/usr/bin/evn python
INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution:
    def check_overflow(self, x):
        if x > INT_MAX or x < INT_MIN:
            return False
        return True
    def get_new_palindrome_x(self, x):
        value = x
        remainder = value%10
        newx = remainder
        value = value/10
        while 0x00 != value:
            newx *=10;
            remainder = value%10
            newx += remainder;
            value = value/10
        return newx
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0x00 or False == self.check_overflow(x):
            return False
        if 0x00 == x:
            return True
        newx = self.get_new_palindrome_x(x)
        return x==newx

if __name__ == '__main__':
    p = Solution();
    value = 12321
    if True == p.isPalindrome(value):
        print "True : %d" % value
    else:
        print 'False : %d' % value



