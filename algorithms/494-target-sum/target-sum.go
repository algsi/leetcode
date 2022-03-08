package problem494

// 回溯
func findTargetSumWays(nums []int, target int) int {
	if len(nums) == 1 {
		r := 0
		if nums[0] == target {
			r++
		}
		if nums[0] == -target {
			r++
		}
		return r
	}

	// backtrack
	r1 := findTargetSumWays(nums[1:], target-nums[0])
	r2 := findTargetSumWays(nums[1:], target+nums[0])
	return r1 + r2
}
