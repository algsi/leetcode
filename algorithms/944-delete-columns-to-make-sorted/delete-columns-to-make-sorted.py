from typing import List

def min__deletion_size(strs: List[str]) -> int:
    row = len(strs)
    col = len(strs[0])
    output = 0
    for j in range(0, col):
        for i in range(1, row):
            if strs[i - 1][j] > strs[i][j]:
                output += 1
                break
    return output
