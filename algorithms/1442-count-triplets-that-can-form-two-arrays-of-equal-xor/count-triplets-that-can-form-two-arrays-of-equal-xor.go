package problem1442

// countTripletsV1 三重循环
func countTripletsV1(arr []int) (ans int) {
	n := len(arr)
	s := make([]int, n+1)
	for i, val := range arr {
		s[i+1] = s[i] ^ val
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j; k < n; k++ {
				if s[i] == s[k+1] {
					ans++
				}
			}
		}
	}
	return
}

// countTripletsV2 哈希表：一重循环
func countTripletsV2(arr []int) (ans int) {
	n := len(arr)
	s := make([]int, n+1)
	for i, v := range arr {
		s[i+1] = s[i] ^ v
	}

	cnt := map[int]int{}
	total := map[int]int{}
	for k := 0; k < n; k++ {
		if m, has := cnt[s[k+1]]; has {
			ans += m*k - total[s[k+1]]
		}
		cnt[s[k]]++
		total[s[k]] += k
	}
	return
}
