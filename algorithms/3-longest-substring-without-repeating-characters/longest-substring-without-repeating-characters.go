package problem3

// 滑动窗口（哈希表）
func lengthOfLongestSubstring(s string) int {
	m := map[byte]int{} // char count
	n := len(s)
	// right point, initialized with 1
	right, ans := -1, 0

	// left point
	for i := 0; i < n; i++ {
		if i != 0 {
			// remove from set
			delete(m, s[i-1])
		}

		// move right point
		for right+1 < n && m[s[right+1]] == 0 {
			m[s[right+1]]++
			right++
		}
		ans = max(ans, right-i+1)
	}

	return ans
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
