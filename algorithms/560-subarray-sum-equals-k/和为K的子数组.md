# 和为K的子数组

LeetCode 560

<https://leetcode.com/problems/subarray-sum-equals-k/>

<https://leetcode-cn.com/problems/subarray-sum-equals-k/>

## 枚举

假设数组最后一个元素的下标为 m。

考虑以 i 开头和为 k 的连续子数组个数，对于某个 i，我们需要确定符合条件的 j 的个数，其中 $0<=i<=j$ 这个子数组的和恰好为K。

我们可以枚举 $[i, m]$ 里所有的下标 $j$ 来判断是否符合条件，你可能会认为我们确定了子数组的开头和末尾，还需要  $O(n)$ 的时间复杂度来计算子数组的和，那样复杂度就将达到 $O(n^3)$，但其实我们又仔细想一想，如果我们知道 $[i, j]$ 子数组的和，就能推出 $[i, j+1]$ 的和，因此这部分的遍历求和是不需要的。

```python
from typing import List

def subarray_sum_1(nums: List[int], k: int) -> int:
    """
    枚举
    考虑以 i 开头和为 k 的连续子数组个数，对于某个 i，我们需要确定符合条件的 j 的个数，其中 0<=i<=j 这个子数组的和恰好为K。

    时间复杂度：平方级
    空间复杂度：常数级
    """

    ans = 0

    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            # 优化求和，减少重复的计算量
            sum += nums[j]
            if sum == k:
                ans += 1

    return ans
```

## 前缀和 + 哈希表优化

我们可以基于方法一利用数据结构进行进一步的优化，我们知道方法一的**瓶颈**在于对每个 $i$，我们需要枚举所有的 $j$ 来判断是否符合条件，这一步是否可以优化呢？答案是可以的。

我们定义 $pre[i]$ 为 $[0..i]$ 里所有数的和，则 $pre[i]$ 可以由 $pre[i−1]$ 递推而来，即：

$$
pre[i] = pre[i-1] + nums[i]
$$

那么 $[j..i]$ 这个子数组和为 $k$ 这个条件我们可以转化为

$$
pre[i] - pre[j-1] = k
$$

简单移项可得符合条件的下标 $j$ 需要满足：

$$
pre[j-1] = pre[i] - k
$$

所以我们考虑以 i 结尾的和为 k 的连续子数组个数时只要统计有多少个前缀和为 $pre[i]−k$ 的 $pre[j]$ 即可。知道了这一条结论，我们建立哈希表 mp，以和为键，出现次数为对应的值，记录 $pre[i]$ 出现的次数，从左往右边更新 mp 边计算答案，那么以 i 结尾的答案 $mp[pre[i]−k]$ 即可在 $O(1)$ 时间内得到。

后的答案即为所有下标结尾的和为 k 的子数组个数之和。

```java
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, pre = 0;
        HashMap < Integer, Integer > mp = new HashMap < > ();
        mp.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            pre += nums[i];
            if (mp.containsKey(pre - k))
                count += mp.get(pre - k);
            mp.put(pre, mp.getOrDefault(pre, 0) + 1);
        }
        return count;
    }
}
```
