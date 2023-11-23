package problem1743

// restoreArray 哈希表
func restoreArray(adjacentPairs [][]int) []int {
	mp := map[int][]int{}
	n := len(adjacentPairs) + 1
	for i := 0; i < n-1; i++ {
		pair := adjacentPairs[i]
		mp[pair[0]] = append(mp[pair[0]], pair[1])
		mp[pair[1]] = append(mp[pair[1]], pair[0])
	}

	ret := make([]int, n, n)

	// 找到首或者尾
	for key, arr := range mp {
		if len(arr) == 1 {
			ret[0] = key
			break
		}
	}

	ret[1] = mp[ret[0]][0]
	for i := 2; i < n; i++ {
		adj := mp[ret[i-1]]
		if ret[i-2] == adj[0] {
			ret[i] = adj[1]
		} else {
			ret[i] = adj[0]
		}
	}
	return ret
}
