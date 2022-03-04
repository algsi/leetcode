"""
20. valid parentheses

有效的括号
"""


def is_valid(s: str) -> bool:
    """
    use stack
    """
    if not s:
        return True

    stack = []
    for e in s:
        if e == '{' or e == '[' or e == '(':
            stack.append(e)
        else:
            if e == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            elif e == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif e == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()

    return len(stack) == 0


def main():
    param = '{[]}'
    r = is_valid(param)
    print(r)


if __name__ == '__main__':
    main()
