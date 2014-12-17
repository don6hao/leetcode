
INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution:
    # @return an integer
    def check_overflow(self, x):
        if x > INT_MAX or x < INT_MIN:
            return 0x00
        return x

    def get_new_value(self, value):
        value_list = []
        sum_value = 0x00
        while 0x00 != value:
            value_list.append(value%10)
            value = value/10
        for i in value_list:
            sum_value = sum_value*10;
            sum_value += i
        return self.check_overflow(sum_value)

    def reverse(self, x):
        if x < INT_MIN or x > INT_MAX:
            return False;
        if x > 0x00:
            return self.get_new_value(x)
        elif x < 0x00:
            return self.get_new_value(abs(x))*-1;
        else:
            return x

if __name__ == '__main__':
    reverse = Solution();
    print reverse.reverse(321);
    print reverse.reverse(0);
    print reverse.reverse(-123);

