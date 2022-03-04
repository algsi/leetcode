"""
43. multiply string

字符串相乘
"""


class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        begin = 0
        res = ''
        for digit in num2[::-1]:
            tmp = self.multiply_one_number(num1, digit, begin)
            res = self.add(res, tmp)
            begin += 1

        return res

    def multiply_one_number(self, num1: str, num2: str, begin: int) -> str:
        """
        the number of num2 only contains one digit.
        """
        if num1 == '0' or num2 == '0':
            return '0'
        carry = 0
        r = ''
        num2 = int(num2)
        for i in num1[::-1]:
            tmp = int(i) * num2 + carry
            carry = tmp // 10
            r = str(tmp % 10) + r

        # attention carry
        if carry > 0:
            r = str(carry) + r
        return r + '0' * begin

    def add(self, num1: str, num2: str) -> str:
        """
        add two string
        """
        res = ''

        # 两个指针，从右往左移动
        # 进位记录
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = 0 if tmp < 10 else 1
            res = str(tmp % 10) + res  # 注意前后顺序
            i, j = i - 1, j - 1

        # 1 必须放在前面，否则字符串的顺序不对
        return '1' + res if carry else res


def main():
    solution = Solution()
    r = solution.multiply('123', '456')
    print(r)
    pass


if __name__ == '__main__':
    main()
