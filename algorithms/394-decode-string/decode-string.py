"""
394. decode strings

https://leetcode-cn.com/problems/decode-string/

字符串解码
"""


def decode_string(s: str) -> str:
    """
    一个栈
    """
    stack = []
    for i in s:
        if i.isdigit():
            # 和前面的数字进行结合
            if len(stack) > 0 and stack[-1].isdigit():
                stack.append(stack.pop() + i)
            else:
                stack.append(i)
            continue
        if i == '[':
            stack.append(i)
            continue
        if i == ']':
            tmp = ''
            e = stack.pop()
            while not e.isdigit():
                if e == '[':
                    e = stack.pop()
                    continue
                tmp = e + tmp
                e = stack.pop()
            tmp *= int(e)
            stack.append(tmp)
        else:
            stack.append(i)

    ans = ''
    while len(stack) != 0:
        ans = stack.pop() + ans
    return ans


def decode_string_2(s: str) -> str:
    """
    数字栈 + 字符栈
    """
    stack_num = []
    stack_str = []
    i = 0
    n = len(s)
    while i < n:
        if s[i].isdigit():
            num = s[i]
            i += 1
            while i < n and s[i] != '[':
                num += s[i]
                i += 1
            stack_num.append(int(num))
            continue
        if s[i] == '[':
            stack_str.append(s[i])
            i += 1
            continue
        if s[i] == ']':
            tmp = ''
            tmp_s = stack_str.pop()
            while tmp_s != '[':
                tmp = tmp_s + tmp
                tmp_s = stack_str.pop()
            stack_str.append(tmp * stack_num.pop())
            i += 1
        else:
            stack_str.append(s[i])
            i += 1

    ans = ''
    while len(stack_str) != 0:
        ans = stack_str.pop() + ans
    return ans


if __name__ == '__main__':
    s1 = decode_string("2[2[y]pq4[2[jk]e11[f]]]ef")
    s2 = decode_string_2("2[2[y]pq4[2[jk]e11[f]]]ef")
    print(s1)
    print(s2)
