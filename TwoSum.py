class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        Dict = {}
        for i in range(len(num)):
            if (target - num[i]) in Dict:
                return (Dict[target - num[i]], i + 1)
            else:
                Dict[num[i]] = i + 1
        return None

if __name__ == '__main__':
    num = [3,2,4]
    target = 6
    p = Solution()
    print p.twoSum(num, target)


