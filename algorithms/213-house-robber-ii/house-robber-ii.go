package problem213

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

// dynamicProgrammingRob 动态规划
func dynamicProgrammingRob(nums []int) int {
	prevMax := 0
	curMax := 0
	for _, num := range nums {
		temp := curMax
		curMax = max(curMax, prevMax+num)
		prevMax = temp
	}

	return curMax
}

func rob(nums []int) int {
	// 分两次动态规划
	// 1. 考虑偷第一间房子，那么最后一间房子一定不能偷
	// 2. 不考虑偷第一间房子
	length := len(nums)
	if length != 1 {
		return max(dynamicProgrammingRob(nums[:len(nums)-1]), dynamicProgrammingRob(nums[1:]))
	} else {
		return nums[0]
	}
}
