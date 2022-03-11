package problem2049

func countHighestScoreNodes(parents []int) int {
	n = len(parents)

	// build tree
	children = make([][]int, n)
	for node, p := range parents {
		if p != -1 {
			children[p] = append(children[p], node)
		}
	}

	maxScore, cnt = 0, 0

	var dfs func(int) int
	dfs = func(node int) int {
		score := 1
		size := n-1

		for _, ch := children[node] {
			sz := dfs(ch)
			score *= sz
			size -= sz 
		}

		if node != 0 {
			score *= size
		}

		if score == maxScore {
			cnt++
		} else if score > maxScore {
			maxScore = score
			cnt = 1
		}

		return n - size
	}

	dfs(0)
	return cnt
}
