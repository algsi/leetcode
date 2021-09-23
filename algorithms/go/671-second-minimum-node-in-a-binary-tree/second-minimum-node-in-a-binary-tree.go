package problem671

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findSecondMinimumValue(root *TreeNode) int {
	ans := -1
	rootVal := root.Val

	var dfsFunc func(node *TreeNode) // dfs function
	dfsFunc = func(node *TreeNode) {
		if node == nil || ans != -1 && node.Val >= ans {
			return
		}
		if node.Val > rootVal {
			ans = node.Val
		}
		dfsFunc(node.Left)
		dfsFunc(node.Right)
	}
	dfsFunc(root)

	return ans
}
