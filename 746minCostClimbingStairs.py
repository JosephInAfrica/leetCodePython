from functools import cache
from typing import List, Tuple



class Solution:
    @cache
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==0:
            return 0
        if len(cost)==1:
            return cost[0]
        if len(cost)==2:
            return min(cost[0],cost[1])
        return self.climbStairs(n-1)+self.climbStairs(n-2)


