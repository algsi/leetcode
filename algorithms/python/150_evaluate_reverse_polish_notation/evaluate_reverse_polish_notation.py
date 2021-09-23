"""
150. evaluate reverse polish notation

https://leetcode.com/problems/evaluate-reverse-polish-notation/
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

逆波兰表达式求值
"""
from operator import mul, add, sub
from typing import List


def eval_prn(tokens: List[str]) -> int:
    op_to_binary_fn = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': lambda x, y: int(x / y)  # 需要注意 python 中负数除法的表现与题目不一致
    }

    n = len(tokens)
    stack = [0] * ((n + 1) // 2)  # 只存储操作数的栈
    index = -1
    for token in tokens:
        if token in op_to_binary_fn:
            # 操作符
            index -= 1
            # call function
            stack[index] = op_to_binary_fn[token](stack[index], stack[index + 1])
        else:
            # 操作数
            num = int(token)
            index += 1
            stack[index] = num

    return stack[0]
