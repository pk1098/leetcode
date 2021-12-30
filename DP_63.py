class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        array = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if (m==1 and n==1) and obstacleGrid[0][0]!=1:
            return 1
        elif (m==1 and n==1) and obstacleGrid[0][0]==1:
            return 0
        elif obstacleGrid[0][0]==1:
            return 0
        
        for i in range(m):
            temp = [-1 for j in range(n)]
            array.append(temp)
            
        def calc(total_count,x,y):
            
            

            if x>m-1 or y>n-1 or obstacleGrid[x][y]==1:
                
                return 0
            
            
            elif array[x][y]!=-1:
                total_count = total_count + array[x][y]
                return total_count
                
            elif x==m-1 and y==n-1:
                total_count = total_count+1
                return total_count
            else:
                ans_left = calc(total_count,x+1,y)
                ans_right = calc(total_count,x,y+1)
                
                if ans_left==0 and ans_right==0:
                    array[x][y]=0
                else:
                    array[x][y]=ans_left + ans_right
                    
                
                total_count = total_count + ans_left + ans_right
                return total_count
            
        total_count = 0
        
        ans_left = calc(total_count,1,0)
        
        ans_right = calc(total_count,0,1)
        
        return ans_left + ans_right
        