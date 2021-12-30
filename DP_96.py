class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        if n==1:
            return 1
        if n==2:
            return 2
        
        store_array = [-1 for i in range(n)]
            
        store_array[0] = 1
        store_array[1] = 2
        
        for j in range(3,n+1):
            ans = 0
            i = 1
            while(i<=j):
                
                left = 1 if (i-1==0) else store_array[(i-2)]
                right = 1 if (j-i ==0) else store_array[(j-i)-1]
                ans = ans + (left*right)
                
                i = i + 1
            store_array[j-1] = ans 
        return store_array[n-1]            
            
            
            
        
        
        