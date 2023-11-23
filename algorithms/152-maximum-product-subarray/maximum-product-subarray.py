"""
152. maximum product subarray

乘积最大子数组
"""

def maxProduct(self, nums: List[int]) -> int:
    """
    dynamic programming
    """
    prev_min = nums[0]
    prev_max = nums[0]
    result = nums[0]

    for n in nums[1:]:
        tmp_min = n * prev_min
        tmp_max = n * prev_max
        cur_max = max(max(n, tmp_min), tmp_max)
        cur_min = min(min(n, tmp_min), tmp_max)
        result = max(result, cur_max)
        prev_max = cur_max
        prev_min = cur_min
    
    return result