package problem226

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 递归
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	left := invertTree(root.Left)
	right := invertTree(root.Right)
	root.Left = right
	root.Right = left
	return root
}
