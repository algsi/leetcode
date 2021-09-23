# Permutations

## LeetCode 46 全排列

题目地址：<https://leetcode-cn.com/problems/permutations/>

题目描述：给定一个 **没有重复** 数字的序列，返回其所有可能的全排列。

示例：

```language
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

设$R={r_1,r_2,r_3, ........, r_n}$是要进行排列的 $n$ 个元素，$R_i=R-{r_i}$。集合 $X$ 中的元素的全排列记为 $Perm(X)$。$(r_i)Perm(X)$ 表示全排列 $Perm(X)$ 的每一个排列前加上前缀 $r_i$ 得到的排列。$R$ 的全排列可归纳定义如下：

- 当 $n=1$ 时，$Perm(R)=(r)$，其中 $r$ 是集合 $R$ 中唯一的元素；

- 当 $n>1$ 时，$Perm(R)$ 由 $(r_1)Perm(R_1), (r_2)Perm(R_2), ..., (r_n)Perm(R_n)$ 构成。

依次递归定义，可设计产生 $Perm(R)$ 的递归算法如下：

```python
"""
46. permutations

全排列
"""

from typing import List


class Solution:
    """
    backtrack 搜索回溯
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(k: int):
            """
            产生 list[k, n] 的所有排列
            """
            if k == n:
                ans.append(nums.copy())
                return

            for i in range(k, n):
                nums[k], nums[i] = nums[i], nums[k]
                backtrack(k + 1)
                # 复原
                nums[k], nums[i] = nums[i], nums[k]

        backtrack(0)
        return ans
```

## LeetCode 47 全排列 Ⅱ

题目地址：<https://leetcode-cn.com/problems/permutations-ii/>

题目描述：给定一个**可包含重复数字**的序列，返回所有不重复的全排列。

示例：

```language
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

这一题和上面一题的区别就是包含了重复的数字，我们用 47 题给出的示例输入到上一题的程序中，给出的输出是：

```language
[[1, 1, 2], [1, 2, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 1, 1]]
```

可以看到，上一题的答案，并不适合这一题，我们需要考虑去重。

当然，要解决这个问题，我们需要找到生成重复的排列的根源。如果我们的序列是：[1, 1, 2]，那么，它的全排列由：{1}[1, 2]，{1}[1, 2]，{2}[1, 1] 组成（第一个是前缀），也就是说，当我们交换元素来产生不同的前缀时，可能会出现重复的元素导致重复的前缀，所以，我们要排除掉这种情况，我们可以使用一个集合来存储在一次递归中交换的元素，交换之前先进行判断，如果该元素在集合中已经存在，说明前面已经由相同的元素交换产生了一个前缀，如果再交换则重复了。只需在上面的程序中稍作修改，加入一个Set集合：

```python
"""
47. permutation ii

全排列 Ⅱ
"""

from typing import List


class Solution:
    """
    backtrack 搜索回溯
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def perm_internal(k: int):
            """
            产生 list[k, n] 的所有排列
            """
            if k == n:
                ans.append(nums.copy())
                return

            # 存储本次递归交换过的元素
            record = set()
            for i in range(k, n):
                if nums[i] in record:
                    continue
                record.add(nums[i])
                nums[k], nums[i] = nums[i], nums[k]
                perm_internal(k + 1)
                # 复原
                nums[k], nums[i] = nums[i], nums[k]

        perm_internal(0)
        return ans
```

