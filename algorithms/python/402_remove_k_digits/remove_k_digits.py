"""
402. remove k digits

https://leetcode.com/problems/remove-k-digits/
https://leetcode-cn.com/problems/remove-k-digits/

移掉K位数字
"""


class Solution:
    """
    贪心 + 单调栈

    complexity analysis
    time complexity: O(N)
    space complexity: O(N)
    """
    def remove_k_digits(self, num: str, k: int) -> str:
        if not num or k <= 0:
            return num
        stack = [num[0]]
        for digit in num[1:]:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        final = stack[:-k] if k else stack
        # 抹去前导零
        return ''.join(final).lstrip('0') or '0'
