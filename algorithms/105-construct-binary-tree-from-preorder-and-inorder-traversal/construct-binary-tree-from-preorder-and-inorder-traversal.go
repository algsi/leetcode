package problem105

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

// 递归。递归构造树以及左右子树
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}

	// 根据前序遍历特点，先找到根节点
	root := &TreeNode{preorder[0], nil, nil}
	i := 0
	for ; i < len(inorder); i++ {
		if inorder[i] == preorder[0] {
			break
		}
	}

	// 递归构建，要分别知道左子树和右子树节点的数量
	leftCount := len(inorder[:i])
	root.Left = buildTree(preorder[1:leftCount+1], inorder[:i])
	root.Right = buildTree(preorder[leftCount+1:], inorder[i+1:])
	return root
}