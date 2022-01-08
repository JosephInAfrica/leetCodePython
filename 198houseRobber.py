from functools import cache
from typing import List, Tuple
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(n:int)->int:
            if n==0:
                return 0
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])
            return max(nums[n-1]+dp(n-2),nums[n-2]+dp(n-3))
        return dp(len(nums))

class Test198(unittest.TestCase):
    def test_Solution(self):
        self.assertEqual(Solution().rob([1,2,3,1]),4)
        self.assertEqual(Solution().rob([2,7,9,3,1]),12)



if __name__=="__main__":
    unittest.main()[2,7,9,3,1]