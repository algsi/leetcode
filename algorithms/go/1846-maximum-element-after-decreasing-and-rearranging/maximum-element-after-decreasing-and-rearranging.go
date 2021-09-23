package problem1846

import "sort"

// maximumElementAfterDecrementingAndRearranging 排序 + 贪心
func maximumElementAfterDecrementingAndRearranging(arr []int) int {
	n := len(arr)
	sort.Ints(arr)
	arr[0] = 1
	for i := 1; i < n; i++ {
		arr[i] = min(arr[i], arr[i-1]+1)
	}
	return arr[n-1]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
