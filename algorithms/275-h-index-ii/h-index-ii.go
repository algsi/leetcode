package problem275

import "sort"

// hIndex use binary search
func hIndex(citations []int) int {
	n := len(citations)
	return n - sort.Search(n, func(x int) bool {
		return citations[x] >= n-x
	})
}
