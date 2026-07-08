class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        previous, current  = 1, 2
        for i in range(3, n+1):
            previous, current = current, previous + current
            print(previous, current)

        return current