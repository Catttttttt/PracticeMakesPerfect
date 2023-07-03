# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1.val
        while l1.next:
            l1 = l1.next
            n1 = 10 * n1 + l1.val
        n2 = l2.val
        while l2.next:
            l2 = l2.next
            n2 = 10 * n2 + l2.val
        n3 = n1 + n2
        s3 = str(n3)
        res = ListNode()
        cpy = res
        for i in s3:
            cpy.next = ListNode()
            cpy = cpy.next
            cpy.val = int(i)            
        return res.next
