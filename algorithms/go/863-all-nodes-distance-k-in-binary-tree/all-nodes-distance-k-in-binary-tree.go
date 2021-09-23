package problem863

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// distanceK 深度优先搜索 + 哈希表
func distanceK(root *TreeNode, target *TreeNode, k int) []int {
	// 从 root 出发 DFS，记录每个结点的父结点
	parents := map[int]*TreeNode{}

	// the function to find parents
	var findParents func(node *TreeNode)
	findParents = func(node *TreeNode) {
		if node.Left != nil {
			parents[node.Left.Val] = node
			findParents(node.Left)
		}
		if node.Right != nil {
			parents[node.Right.Val] = node
			findParents(node.Right)
		}
	}
	findParents(root)

	var ans []int
	// 从 target 出发 DFS，寻找所有深度为 k 的结点
	var findAns func(*TreeNode, *TreeNode, int)
	findAns = func(node *TreeNode, from *TreeNode, depth int) {
		if node == nil {
			return
		}
		if depth == k { // 将所有深度为 k 的结点的值计入结果
			ans = append(ans, node.Val)
			return
		}
		if node.Left != from {
			findAns(node.Left, node, depth+1)
		}
		if node.Right != from {
			findAns(node.Right, node, depth+1)
		}
		if parents[node.Val] != from {
			findAns(parents[node.Val], node, depth+1)
		}
	}
	findAns(target, nil, 0)
	return ans
}
