package problem413

func numberOfArithmeticSlices(nums []int) int {
	n := len(nums)
	if n == 1 {
		return 0
	}
	d := nums[0] - nums[1]
	t := 0
	ans := 0

	for i := 2; i < n; i++ {
		if nums[i-1]-nums[i] == d {
			t += 1
		} else {
			d = nums[i-1] - nums[i]
			t = 0
		}
		ans += t
	}

	return ans
}
