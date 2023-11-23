package problem687

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestUnivaluePath(root *TreeNode) (ans int) {
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		left := dfs(node.Left)
		right := dfs(node.Right)
		leftPath := 0
		if node.Left != nil && node.Left.Val == node.Val {
			leftPath = left + 1
		}
		rightPath := 0
		if node.Right != nil && node.Right.Val == node.Val {
			rightPath = right + 1
		}

		ans = max(ans, leftPath+rightPath)
		return max(leftPath, rightPath)
	}

	dfs(root)
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
