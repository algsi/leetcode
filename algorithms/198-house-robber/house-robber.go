package problem198

func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	n := len(nums)
	if len(nums) == 1 {
		return nums[0]
	}
	first := nums[0]
	second := max(nums[0], nums[1])
	for i := 2; i < n; i++ {
		first, second = second, max(first + nums[i], second)
	}
	
	return second
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}