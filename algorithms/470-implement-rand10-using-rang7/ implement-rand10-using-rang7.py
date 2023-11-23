def rand7() -> int:
    pass


def rand10() -> int:
    while True:
        row = rand7()
        col = rand7()
        idx = (row - 1) * 7 + col
        if idx <= 40:
            return 1 + (idx - 1) % 10
