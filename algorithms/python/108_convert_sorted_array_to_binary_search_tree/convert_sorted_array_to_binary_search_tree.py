"""
108. convert sorted array to binary search tree

将有序数组转换为二叉搜索树
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    """
    递归
    """

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.__internal(nums, 0, len(nums) - 1)

    def __internal(self, nums: List[int], lo: int, hi: int) -> TreeNode:
        """
        递归转换高度平衡二叉搜索树
        """
        if lo == hi:
            return TreeNode(nums[lo])
        elif lo > hi:
            return None
        mid = (lo + hi) // 2
        # 当前树的根节点
        cur_node = TreeNode(nums[mid])
        # 左右子树
        cur_node.left = self.__internal(nums, lo, mid - 1)
        cur_node.right = self.__internal(nums, mid + 1, hi)
        return cur_node
