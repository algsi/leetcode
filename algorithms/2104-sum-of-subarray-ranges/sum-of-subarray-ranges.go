package problem2104

// 暴力
func subArrayRanges(nums []int) int64 {
	length := len(nums)
	var result int64 = 0
	for i, m := range nums {
		max := m
		min := m
		for j := i + 1; j < length; j++ {
			if nums[j] > max {
				max = nums[j]
			}
			if nums[j] < min {
				min = nums[j]
			}
			result += int64(max - min)
		}
	}
	return result
}
