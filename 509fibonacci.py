from typing import List, Tuple
from functools import cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n==0:
        	return 0
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
    

if __name__=="__main__":
	print(Solution().fib(20))