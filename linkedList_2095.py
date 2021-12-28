# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp_prev = None
        size = 0
        middle = 0
        values = []
        
        if head.next == None:
            head = None
            return head
        
        while(temp!=None):
            size = size + 1
            values.append(temp)
            temp = temp.next
        if size%2 != 0:
            middle = ((size+1)/2)-1
        else:
            middle = size/2
        
        
        temp = values[int(middle)]
        temp_prev = values[int(middle-1)]
        temp_prev.next = temp.next
        
        return head