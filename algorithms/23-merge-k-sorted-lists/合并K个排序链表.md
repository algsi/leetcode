# 合并K个排序链表

LeetCode 23

<https://leetcode-cn.com/problems/merge-k-sorted-lists/>

<https://leetcode.com/problems/merge-k-sorted-lists/>

## 前置知识

合并两个有序链表

LeetCode 21

```python
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    迭代：伪头节点的应用
    时间复杂度：O(n + m)
    空间复杂度：O(1)
    """
    dummy = ListNode(-1)
    prev = dummy
    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next

    # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 if l1 is not None else l2

    return dummy.next

```

## Approach 1: merge lists one by one

顺序合并

我们可以想到一种最朴素的方法：用一个变量 `ans` 来维护以及合并的链表，第 $i$ 次循环把第 $i$ 个链表和 `ans` 合并，答案保存到 `ans` 中。

```python
def merge_k_lists_1(lists: List[ListNode]) -> ListNode:
    """
    方法一
    merge list one by one(顺序合并)
    """
    ans = None
    for l in lists:
        ans = merge_two_lists(ans, l)
    return ans
```

复杂度：

- 时间复杂度

  假设每个链表的最长长度是 $n$。在第一次合并后，`ans` 的长度为 $n$；第二次合并后，`ans` 的长度为 $2×n$，第 $i$ 次合并后，`ans` 的长度为 $i×n$。第 i*i* 次合并的时间代价是 $O(n+(i-1)×n)=O(i×n)$，那么可以推出总的代价为
  $$
  O(\sum_1^k(k×n))=O(\frac{(1+k)k}{2}×n)=O(k^2×n)
  $$
  故渐进时间复杂度为$O(k^2×n)$

- 空间复杂度：没有用到与 $k$ 和 $n$ 规模相关的辅助空间，故渐进空间复杂度为 $O(1)$。

## Approach 2: merge with divide and conquer

分治合并

我们知道，归并排序有一种自底向上的实现方法（非递归），其核心思想就是先把一个数组划分成多个小数组并让它们两两合并，得到的结果再两两合并，最终使得整个数组有序。

在这里我们也可以这样做，如下图：

<img src="images/6f70a6649d2192cf32af68500915d84b476aa34ec899f98766c038fc9cc54662-image.png" alt="img"  />

代码

```python
def merge(lists: List[ListNode], lo, hi) -> ListNode:
    """
    merge lists from lo(inclusive) to hi(inclusive)
    """
    if lo == hi:
        return lists[lo]

    # 这一步判断是必要的，避免lists为空列表出现的异常
    if lo > hi:
        return None

    mid = (hi - lo) // 2 + lo

    return merge_two_lists(merge(lists, lo, mid), merge(lists, mid + 1, hi))


def merge_k_lists_2(lists: List[ListNode]) -> ListNode:
    """
    方法二
    merge with divide and conquer(分治合并)
    类似于非递归版本的归并排序（自底向上归并排序）
    """
    return merge(lists, 0, len(lists) - 1)
  
def merge_k_lists_3(lists: List[ListNode]) -> ListNode:
    """
    方法二（非递归实现）
    merge with divide and conquer(分治合并)
    类似于自底向上归并排序
    """
    amount = len(lists)

    # 归并间隙，成倍增长
    interval = 1

    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists
```

这里分析非递归版本实现的复杂度。

Complexity Analysis

- Time Complexity: $O(Nlogk)$ where k is the number of linked lists.

  We can merge two sorted linked list in $O(n)$ time where n*n* is the total number of nodes in two lists.

- Space complexity : $O(1)$

  We can merge two sorted linked lists in $O(1)$  space.

