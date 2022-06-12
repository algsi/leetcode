def min_flips_mono_incr(s: str) -> int:
    dp0, dp1 = 0, 0
    for c in s:
        dp0_new, dp1_new = dp0, min(dp0, dp1)
        if c == '1':
            dp0_new += 1
        else:
            dp1_new += 1
        dp0, dp1 = dp0_new, dp1_new
    return min(dp0, dp1)
