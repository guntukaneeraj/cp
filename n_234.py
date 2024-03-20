#234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while head:
            l.append(head)
            head=head.next
        i=0
        j=len(l)-1
        flag=True
        while i<j:
            if (l[i].val!=l[j].val):
                flag=False
                break
            i+=1
            j-=1
        return flag
