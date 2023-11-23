"""
104. maximum depth of binary tree

二叉树的最大深度
"""


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


def max_depth(root: TreeNode) -> int:
    """
    递归

    complexity analysis
    time complexity: O(n)
    space complexity: O(n). 递归栈所需要的空间
    """

    if root is None:
        return 0

    # 分别求左右子树的最大深度
    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


def max_depth_2(root: TreeNode) -> int:
    """
    非递归

    用队列实现的二叉树的层序遍历（BFS 广度优先遍历）

    时间复杂度：O(N)
    空间复杂度：O(N)
    """
    if root is None:
        return 0

    queue = [root]
    depth = 0

    # 上一层的元素个数
    num_of_last_level = 1

    while len(queue) != 0:
        depth += 1
        count = 0

        # 把上一层的元素都出队，下一层的元素入队
        while num_of_last_level != 0:
            node = queue.pop(0)
            num_of_last_level -= 1

            if node.left is not None:
                queue.append(node.left)
                count += 1
            if node.right is not None:
                queue.append(node.right)
                count += 1

        num_of_last_level = count

    return depth


def max_depth_3(root: TreeNode) -> int:
    """
    非递归

    用栈实现的DFS（深度优先遍历）

    我们从包含根结点且相应深度为 1 的栈开始。然后我们继续迭代：将当前结点弹出栈并推入子结点。每一步都会更新深度。

    时间复杂度：O(N)
    空间复杂度：O(N)
    """

    stack = []
    if root is not None:
        stack.append((1, root))

    depth = 0
    while len(stack) != 0:
        current_depth, root = stack.pop()
        depth = max(current_depth, depth)
        if root.left is not None:
            stack.append((current_depth + 1, root.left))
        if root.right is not None:
            stack.append((current_depth + 1, root.right))

    return depth
