class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = list(str(num))
        e = list()
        o = list()
        for i in a:
            i = int(i)
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        res = []
        for i in range(len(a)):
            m = 0
            if int(a[i]) % 2 == 0:
                m = max(e)
                e.remove(m)
            else:
                m = max(o)
                o.remove(m)
            res.append(str(m))
        res = ''.join(res)
        return int(res)
