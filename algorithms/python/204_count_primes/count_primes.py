"""
204. count primes

https://leetcode.com/problems/count-primes/
https://leetcode.com/problems/count-primes/

计数质数
"""


class Solution:
    def count_primes(self, n: int) -> int:
        is_prime = [1] * n
        output = 0
        for i in range(2, n):
            if is_prime[i] == 1:
                output += 1
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        return output


def main():
    solution = Solution()
    n = 499979
    r = solution.count_primes(n)
    print(r)


if __name__ == '__main__':
    main()
