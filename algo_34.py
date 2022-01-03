class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        flag = 0
        
        while(left<=right):
            
            mid = int((right+left)/2)
            
            if nums[mid]==target:
                flag = 1
                break
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        l_index = mid
        r_index = mid
        if flag == 0:      
            return [-1,-1]
        else:
            i = mid-1
            j = mid+1
            while((i>=0 and nums[i]==target)):
                l_index = i
                i = i-1
                
            while (j<=right and nums[j]==target):
                r_index = j
                j = j + 1
        return [l_index,r_index]
                
        