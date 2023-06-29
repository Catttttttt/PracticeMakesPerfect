class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        s = 0
        two = 0
        for i in range(n):
            if colsum[i] == 2:
                two += 1
            s += colsum[i]
        if two > upper or two > lower or s != upper + lower:
            return []        
        upper -= two
        lower -= two
        matrix = [[0] * n, [0] * n]
        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
            elif colsum[i] == 1:
                if upper > 0:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    matrix[1][i] = 1         
        return matrix
