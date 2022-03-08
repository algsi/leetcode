package problem2055

func platesBetweenCandles(s string, queries [][]int) []int {
	n := len(s)
	preSum := make([]int, n) // 前缀和
	left := make([]int, n)   // 左边第一根蜡烛所在的下标
	right := make([]int, n)  // 右边第一根蜡烛所在的下标

	sum, l := 0, -1
	for i, ch := range s {
		if ch == '*' {
			sum++
		} else {
			l = i
		}
		preSum[i] = sum
		left[i] = l
	}

	for i, r := n-1, -1; i >= 0; i-- {
		if s[i] == '|' {
			r = i
		}
		right[i] = r
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		x, y := right[q[0]], left[q[1]]
		if x >= 0 && y >= 0 && x < y {
			ans[i] = preSum[y] - preSum[x]
		}
	}
	return ans
}
