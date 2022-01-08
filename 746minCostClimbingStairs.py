from functools import cache
from typing import List, Tuple



class Solution:
    def minCostClimbingStairs(self, cost: Tuple[int]) -> int:
        @cache
        # dp(n) mean finish first n floor
        def dp(n:int)->int:
            if n<2:
                return 0

            return min(cost[n-1]+dp(n-1),cost[n-2]+dp(n-2))
        
        return dp(len(cost))


if __name__=="__main__":
    print(Solution().minCostClimbingStairs([10,15,20]))


