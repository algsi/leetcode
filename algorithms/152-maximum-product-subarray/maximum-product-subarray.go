package problem152

// dynamic programming
func maxProduct(nums []int) int {
	prevMin := nums[0]
	prevMax := nums[0]
	result := nums[0]

	for _, n := range nums[1:] {
		tmpMin := n * prevMin
		tmpMax := n * prevMax
		curMin := min(min(n, tmpMax), tmpMin)
		curMax := max(max(n, tmpMax), tmpMin)
		result = max(result, curMax)
		prevMax = curMax
		prevMin = curMin
	}

	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
