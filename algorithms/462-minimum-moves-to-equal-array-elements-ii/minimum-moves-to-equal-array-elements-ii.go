package prblem462

import "sort"

func minMoves2(nums []int) (ans int) {
	sort.Ints(nums)
	x := nums[len(nums)/2]
	for _, num := range nums {
		ans += abs(x - num)
	}
	return
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
