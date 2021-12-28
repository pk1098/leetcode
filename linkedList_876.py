# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        size = 0
        middle = 0
        values = []
        while(temp!=None):
            size = size + 1
            values.append(temp)
            temp = temp.next
        if size%2 != 0:
            middle = ((size+1)/2)-1
        else:
            middle = size/2
        
        return values[int(middle)]# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        size = 0
        middle = 0
        values = []
        while(temp!=None):
            size = size + 1
            values.append(temp)
            temp = temp.next
        if size%2 != 0:
            middle = ((size+1)/2)-1
        else:
            middle = size/2
        
        return values[int(middle)]