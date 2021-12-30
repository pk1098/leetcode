class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        array = []
        m = len(grid)
        n = len(grid[0])
        
        if m==1 and n==1:
            return grid[0][0]
        
        for i in range(m):
            temp = [-1 for j in range(n)]
            array.append(temp)
            
        def calc(x,y):
            if x>m-1 or y>n-1:
                return 999999
        
            elif array[x][y]!=-1:
                 
                return  array[x][y]  
                
            elif x==m-1 and y==n-1:
                
                return grid[x][y]
            else:
                
                ans_left = calc(x+1,y)
                ans_right = calc(x,y+1)
                
              
                if ans_left==999999 and ans_right==999999:
                    array[x][y]=999999
                else:
                    left_subtree_cost = (ans_left + grid[x][y]) if ans_left!=999999 else 999999
                    right_subtree_cost = (ans_right + grid[x][y]) if ans_right!=999999 else 999999
                    array[x][y] = left_subtree_cost if left_subtree_cost<right_subtree_cost else right_subtree_cost
                    
                
                
                return array[x][y]
            
        ans_left = calc(1,0)
        ans_right = calc(0,1)
        
        
        
        if ans_left==999999 and ans_right==999999:
                    array[0][0]=999999
        else:
            left_subtree_cost = (ans_left + grid[0][0]) if ans_left!=999999 else 999999
            right_subtree_cost = (ans_right + grid[0][0]) if ans_right!=999999 else 999999
            array[0][0] = left_subtree_cost if left_subtree_cost<right_subtree_cost else right_subtree_cost
            
            
        
            
        return array[0][0]