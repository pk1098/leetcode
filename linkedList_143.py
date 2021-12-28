# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        temp_prev = None
        temp_next = None
        size = 0
        middle = 0
        values = []
        
        
        while(temp!=None):
            size = size + 1
            values.append(temp)
            temp = temp.next
            
        if size==1 or size==2:
            return
        elif size%2 != 0:
            middle = ((size+1)/2)-1
        else:
            middle = size/2
        
        temp = head
        index = size-1
        while(middle!=index):
            temp_next = temp.next
            temp.next = values[index]
            values[index].next = temp_next
            temp = temp_next
            index = index - 1
        
        values[int(middle)].next = None
        
        # temp = values[int(middle)]
        # temp_prev = values[int(middle-1)]
        # temp_prev.next = temp.next
        
        return 
        