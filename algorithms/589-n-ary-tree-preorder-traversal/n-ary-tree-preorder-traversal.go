package problem589

type Node struct {
	Val      int
	Children []*Node
}

// 递归
func preorder(root *Node) []int {
	var ans []int
	var dfs func(node *Node)
	dfs = func(node *Node) {
		if node == nil {
			return
		}
		ans = append(ans, node.Val)
		for _, ch := range node.Children {
			dfs(ch)
		}
	}

	dfs(root)
	return ans
}

// 迭代
func preorderV2(root *Node) []int {
	var ans []int
	stack := []*Node{}
    nextIndex := map[*Node]int{}
	node := root
	for len(stack) > 0 || node != nil {
		for node != nil {
			ans = append(ans, node.Val)
			stack = append(stack, node)
			if len(node.Children) == 0 {
				break
			}
			nextIndex[node] = 1
			node = node.Children[0]
		}
		node = stack[len(stack)-1]
		i := nextIndex[node]
		if i < len(node.Children) {
			nextIndex[node] = i + 1
			node = node.Children[i]
		} else {
			stack = stack[:len(stack)-1]
			delete(nextIndex, node)
			node = nil
		}
	}
	return ans
}
