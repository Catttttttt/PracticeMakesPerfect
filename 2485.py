class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n, 0, -1):
            print(i)
            if sum([j for j in range(1, i+1)]) == sum([j for j in range(n, i-1, -1)]):
                return i
        return -1
