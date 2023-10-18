class Solution(object):
    def handleQuery(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for query in queries:
            if query[0] == 1:
                for i in range(query[1], query[2]+1):
                    nums1[i] = not nums1[i]
            elif query[0] == 2:
                for i in range(len(nums1)):
                    nums2[i] = nums2[i] + nums1[i] * query[1]
            else:
                s = sum(nums2)
                ans.append(s)
        return ans

'''
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        cnt1 = [0] * (4 * n)
        flip = [False] * (4 * n)

        # 维护区间 1 的个数
        def maintain(o: int) -> None:
            cnt1[o] = cnt1[o * 2] + cnt1[o * 2 + 1]

        # 执行区间反转
        def do(o: int, l: int, r: int) -> None:
            cnt1[o] = r - l + 1 - cnt1[o]
            flip[o] = not flip[o]

        # 初始化线段树   o,l,r=1,1,n
        def build(o: int, l: int, r: int) -> None:
            if l == r:
                cnt1[o] = nums1[l - 1]
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o)

        # 反转区间 [L,R]   o,l,r=1,1,n
        def update(o: int, l: int, r: int, L: int, R: int) -> None:
            if L <= l and r <= R:
                do(o, l, r)
                return
            m = (l + r) // 2
            if flip[o]:
                do(o * 2, l, m)
                do(o * 2 + 1, m + 1, r)
                flip[o] = False
            if m >= L: update(o * 2, l, m, L, R)
            if m < R: update(o * 2 + 1, m + 1, r, L, R)
            maintain(o)

        build(1, 1, n)
        ans, s = [], sum(nums2)
        for op, l, r in queries:
            if op == 1: update(1, 1, n, l + 1, r + 1)
            elif op == 2: s += l * cnt1[1]
            else: ans.append(s)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/handling-sum-queries-after-update/solutions/2119436/xian-duan-shu-by-endlesscheng-vx80/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''