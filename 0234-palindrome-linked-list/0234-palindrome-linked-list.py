# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        cur = slow
        while cur:
            fwd = cur.next
            cur.next = pre
            pre = cur
            cur = fwd
        left = head
        right = pre
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         list1 = []
#         temp = head
#         while temp:
#             list1.append(temp.val)
#             temp = temp.next
#         i = 0
#         j = len(list1)-1
#         while i < j:
#             if list1[i] != list1[j]:
#                 return False
#             i +=1
#             j -= 1
#         return True
    
    