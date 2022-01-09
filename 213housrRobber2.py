import unittest
from functools import cache
from typing import List, Tuple


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dpC(a: int, b: int) -> int:
            # a: start index of num,  b-1 should be last index
            if b-a <= 0:
                return 0
            if b-a == 1:
                return nums[a]
            if b-a == 2:
                return max(nums[a], nums[a+1])

            m = max(nums[b-1]+dpC(a, b-2), nums[b-2]+dpC(a, b-3))
            # print(nums[a:b], m)
            return m

        # @cache
        # def dp(a: int, b: int) -> int:
        #     if b-a <= 2:
        #         return dpC(a, b)
        #     return max(nums[0]+dpC(2, len(nums)-1), nums[-1]+dpC(1, len(nums)-2), dpC(1, len(nums)-1))

        # if len(nums) <= 2:
        #     return dpC(0, len(nums))

        # return dp(0, len(nums))

        return max(dpC(0, len(nums)-1), dpC(1, len(nums)))
        # return max(nums[b-1]+dpC(a+1, b-2), nums[b-2]+dpC(a, b-3))


class Test198(unittest.TestCase):
    def test_Solution(self):
        self.assertEqual(Solution().rob([2, 3, 2]), 3)
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)
        self.assertEqual(Solution().rob([200, 3, 140, 20, 10]), 340)
        self.assertEqual(Solution().rob([6, 6, 4, 8, 4, 3, 3, 10]), 27)


if __name__ == "__main__":
    unittest.main()
