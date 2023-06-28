class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x ** n
        def mp(x,n):
            if n == 0:
                return 1
            y = mp(x, n//2)
            if n % 2 == 0:
                return y * y
            else:
                return x * y * y
        return mp(x, n) if n >=0 else 1/mp(x, -n)
