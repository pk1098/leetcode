# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        size = 0
        middle = 0
        values = []
        
        while(temp!=None):
            size = size + 1
            values.append(temp)
            temp = temp.next
            
        if head.next==None:
            return head
            
        elif size%2 != 0:
            middle = ((size+1)/2)
            
            if middle==k:
                return head
            else:
                temp_var = values[k-1].val
                values[k-1].val = values[-k].val
                values[-k].val = temp_var
        else:
            temp_var = values[k-1].val
            values[k-1].val = values[-k].val
            values[-k].val = temp_var
            
        
        return head