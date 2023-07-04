class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        res = 0
        while nums:
            m = 0
            for i in nums:
                if not i:
                    return res
                m = max(m,max(i))
                i.remove(max(i))
            res += m
