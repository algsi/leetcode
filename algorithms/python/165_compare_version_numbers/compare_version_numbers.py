def compare_version(version1: str, version2: str) -> int:
    """
    双指针
    """
    n, m = len(version1), len(version2)
    i, j = 0, 0
    base = ord('0')
    while i < n or j < m:
        x = 0
        while i < n and version1[i] != '.':
            x = x * 10 + ord(version1[i]) - base
            i += 1
        i += 1
        y = 0
        while j < m and version2[j] != '.':
            y = y * 10 + ord(version2[j]) - base
            j += 1
        j += 1

        if x > y:
            return 1
        if x < y:
            return -1
    return 0
