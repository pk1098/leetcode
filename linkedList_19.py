# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        temp_prev = None
        size = 0
        middle = 0
        values = []
        
        if head.next == None and n==1:
            head = None
            return head
        
        while(temp!=None):
            size = size + 1
            values.append(temp)
            temp = temp.next
            
        if values[-n] == head:
            head = values[-n].next
        else:
            prev_index = n+1
            values[-prev_index].next = values[-n].next
        
        return head
        