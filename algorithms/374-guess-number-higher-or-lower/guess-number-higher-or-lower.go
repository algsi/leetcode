package problem374

import "sort"

func guessNumber(n int) int {
	// binary search
	return sort.Search(n, func(x int) bool { return guess(x) <= 0 })
}

func guess(num int) int {
	return 0
}
