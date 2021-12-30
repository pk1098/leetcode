class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1 for i in range(len(cost))]
        
        
        def step(index):
            
            
            
            if index>(len(cost)-1):
                return 0
            
            elif(memo[index]!=-1):
                return memo[index]
            
            else:
            
                step_1_cost = step(index + 1)
                step_2_cost = step(index + 2)
                
                if step_1_cost==999999 and step_2_cost==999999:
                    memo[index]=999999
                else:
                    left_subtree_cost = (step_1_cost + cost[index]) if step_1_cost!=999999 else 999999
                    right_subtree_cost = (step_2_cost + cost[index]) if step_2_cost!=999999 else 999999
                    memo[index] = left_subtree_cost if left_subtree_cost<right_subtree_cost else right_subtree_cost
                    
            return memo[index]
            
        
        step_1_cost = step(0)
        step_2_cost = step(1)
        
        if step_1_cost==999999 and step_2_cost==999999:
                    memo[0]=999999
        else:
            left_subtree_cost = (step_1_cost ) if step_1_cost!=999999 else 999999
            right_subtree_cost = (step_2_cost ) if step_2_cost!=999999 else 999999
            memo[0] = left_subtree_cost if left_subtree_cost<right_subtree_cost else right_subtree_cost
            
            
        return memo[0]