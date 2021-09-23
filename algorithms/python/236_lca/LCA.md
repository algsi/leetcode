# LCA

lowest common ancestor of a binary tree (二叉树的最近公共祖先)

## 1. Recursion

我们递归遍历整颗二叉树，定义 $f_x$ 表示 $x$ 节点的子树中是否包含 $p$ 节点或者 $q$ 节点，如果包含为 true，否则为 false，那么符合条件的最近公共祖先 $x$ 一定满足如下条件：

$$
(f_{lson} \ and  \ f_{rson}) || ((x = p \ or \ x = q) \ and \ (f_{lson} \ or  \ f_{rson}))
$$

其中 lson 和 rson 分别代表 $x$ 的左孩子和右孩子。初看可能会感觉条件判断有点复杂，我们来一条条看，$f_{lson} \ and f_{rson}$ 表示左子树和右子树均包含 $p$ 节点或者 $q$ 节点，如果左子树包含的是 $p$ 节点，那么右子树只能包含 $q$ 节点，反之亦然，因为 $p$ 节点和 $q$ 节点都是不同且唯一的节点，因此如果满足了这个判断条件即可说明 $x$ 就是我们要找的最近公共祖先。再来看第二条判断条件，这个条件即是考虑了 $x$ 恰好是 $p$ 节点或者 $q$ 节点且它的左子树或者右子树有一个包含了另一个节点的情况，因此如果满足了这个判断条件亦可以说明 $x$ 就是我们要找的最近公共祖先。

你可能会疑惑这样找出来的公共祖先深度是否是最大的。其实是最大的，因为我们是自底向上从叶子节点开始更新的，所以在所有满足条件的公共祖先中一定是深度最大的祖先先被访问到，且由于 $f_x$ 本身的定义很巧妙，在找到最近公共祖先 $x$ 后，$f_x$ 就被定义设置为 true，即假定了这个子树中只有一个 $p$ 节点或 $q$ 节点，因此其他公共祖先不会再被判断为符合条件。

### 1.1. Java实现

```java
class Solution {

    private TreeNode ans;

    public Solution() {
        this.ans = null;
    }

    private boolean dfs(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return false;
        boolean lson = dfs(root.left, p, q);
        boolean rson = dfs(root.right, p, q);
        if ((lson && rson) || ((root.val == p.val || root.val == q.val) && (lson || rson))) {
            ans = root;
        } 
        return lson || rson || (root.val == p.val || root.val == q.val);
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        this.dfs(root, p, q);
        return this.ans;
    }
}
```

### 1.2. Python实现

```python
class Solution:
    """
    递归 DFS

    complexity analysis
    time complexity: O(N)
    space complexity: O(N)
    """

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def dfs(node: TreeNode):
            """
            DFS the tree

            :return f(node), true indicate that the node's subtree contains p or q
            """
            if node is None:
                return False
            l_son = dfs(node.left)  # f(left_son)
            r_son = dfs(node.right)  # f(right_son)
            if (l_son and r_son) or ((node.val == p.val or node.val == q.val) and (l_son or r_son)):
                nonlocal ans
                # find the lca
                ans = node

            return l_son or r_son or node.val == p.val or node.val == q.val

        dfs(root)
        return ans
```

## 2. Recursion

要解决最近公共祖先问题，我们首先要明白什么是最近的公共祖先，下面先给出两个定义。

**祖先的定义**：若节点 p 在节点 root 的左（右）子树中，或者 p==root，则称 root 是 p 的祖先。

**最近公共祖先的定义**：设节点 root 为节点 p，q 的某公共祖先，若其左子节点 root.left 和右子节点 root.right 都不是 p 和 q 的公共祖先，则称 root 是 p 和 q 的公共祖先。

根据以上的定义，若 root 是 p，q 的最近公共祖先，则可能为以下几种情况之一：

1. p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
2. p == root，且 q 在 root 的左或右子树中；
3. q == root，且 p 在 root 的左或右子树中；
