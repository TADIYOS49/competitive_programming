# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = self.t = ListNode()
        def rec(x,y):
            if x == None:
                return y
            if y == None:
                return x
            if x.val <= y.val:
                self.t.next = ListNode(x.val)
                x = x.next
            else:
                self.t.next = ListNode(y.val)
                y = y.next
            self.t = self.t.next
            return rec(x,y)
        b = rec(list1,list2)
        self.t.next = b
        return ans.next