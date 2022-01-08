from typing import List, Tuple
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def dp(i: int) -> Tuple[int, int]:
            # if i < 0:
            #     return 0, 10**9

            if i == 0:
                return 0, prices[0]
            profit, price = dp(i-1)
            return max(profit, prices[i]-price), min(prices[i], price)

        return dp(len(prices)-1)[0]


if __name__ == "__main__":
    print(Solution().maxProfit([1, 2, 3, 4, 5]))

