"""
657. robot return to origin

机器人能否返回原点
"""


def judge_circle(moves: str) -> bool:
    """
    模拟移动
    """
    if not moves:
        return True
    director = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    x, y = 0, 0
    for m in moves:
        x_i, y_i = director[m]
        x += x_i
        y += y_i

    return x == 0 and y == 0


def judge_circle_2(moves: str) -> bool:
    """
    X轴 and Y轴
    """
    if not moves:
        return True

    x_offset, y_offset = 0, 0
    for m in moves:
        if m == 'R':
            x_offset += 1
        elif m == 'L':
            x_offset -= 1
        elif m == 'U':
            y_offset += 1
        else:
            y_offset -= 1

    return x_offset == 0 and y_offset == 0
