# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1 2 3 4 5  k = 3
    
        """
        check = head
        if k == 1:
            return head
        leng = 0
        while check:
            leng +=1
            check = check.next
        check = head
        ans = ListNode()
        test = ans
        leng = leng//k
        count = k
        while leng > 0:
            prev = None
            while count >=1:
                fwd = check.next
                check.next = prev
                prev = check
                check = fwd
                count -= 1
            test.next = prev
            for i in range(k):
                test = test.next
            leng -= 1
            count = k
        test.next = check
        return ans.next