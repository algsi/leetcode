"""
337. House Robber III

打家劫舍 III
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    """
    递归

    time complexity: O(N)
    space complexity: O(N)
    """

    def rob(self, root: TreeNode) -> int:
        return max(*self.rob_internal(root))

    def rob_internal(self, cur: TreeNode) -> list:
        """
        尝试从该节点开始，尝试获取最多的金钱

        返回一个长度为2的一维数组，数组第一个元素表示不偷当前节点所能得到的最大金钱数量，数组的第二个元素表示偷当前节点所能得到的最大金钱数量
        """
        if not cur:
            return [0, 0]

        result = [0, 0]

        # 从该节点的左子节点开始尝试
        left = self.rob_internal(cur.left)
        # 从该节点的右子节点开始尝试
        right = self.rob_internal(cur.right)

        # 不偷当前节点，则考虑两个孩子节点的情况（孩子节点可偷可不偷）, 取左右两个孩子所能得到能得到的最大值之和
        result[0] = max(*left) + max(*right)

        # 偷当前节点，则两个左右子节点不能偷
        result[1] = left[0] + right[0] + cur.val

        return result
