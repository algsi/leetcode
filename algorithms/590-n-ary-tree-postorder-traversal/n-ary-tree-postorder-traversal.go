package problem590

type Node struct {
    Val int
    Children []*Node
}

func postorder(root *Node) []int {
	if root == nil {
		return []int{}
	}

	var result []int
	for _, ch := range root.Children {
		result = append(result, postorder(ch)...)
	}
	result = append(result, root.Val)
	return result
}

func postorderV2(root *Node) []int {
	if root == nil {
		return []int{}
	}
	st := []*Node{}
	var ans []int
	for len(st) > 0 {
		node := st[len(st)-1]
		st = st[:len(st)-1]
		ans = append(ans, node.val)
		st = append(st, node.Children...)
	}
	for i, n := 0, len(ans); i < n/2; i++ {
        ans[i], ans[n-1-i] = ans[n-1-i], ans[i]
    }
    return ans
}
