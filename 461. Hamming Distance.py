# 用时12:34，还是参考了别人的想法
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        count = 0

        c = str(bin(x ^ y))
        for i in c:
            if i == '1':
                count += 1
        return count
