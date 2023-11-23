package problem199

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type pair struct {
	node  *TreeNode
	depth int
}

func rightSideView(root *TreeNode) []int {
	// 深度为索引，存放节点的值
	rightMostValueAtDepth := make(map[int]int)
	stack := []pair{{root, 0}}
	maxDepth := -1

	for len(stack) > 0 {
		// pop
		p := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		node, depth := p.node, p.depth

		if node != nil {
			maxDepth = max(maxDepth, depth)

			if _, ok := rightMostValueAtDepth[depth]; !ok {
				rightMostValueAtDepth[depth] = node.Val
			}
			stack = append(stack, pair{node.Left, depth + 1})
			stack = append(stack, pair{node.Right, depth + 1})
		}
	}

	var ans []int
	for i := 0; i <= maxDepth; i++ {
		ans = append(ans, rightMostValueAtDepth[i])
	}
	return ans
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
