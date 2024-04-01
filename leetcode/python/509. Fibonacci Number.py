class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        fib1, fib2 = 1, 1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2
