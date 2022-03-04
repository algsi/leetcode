package problem53

// maxSubArray 动态规划
// definition: f(x) 为代表以第 i 个数结尾的连续子数组的最大和
// f(i) = max{f(i - 1) + num[i], num[i]}
func maxSubArray(nums []int) int {
	cur := nums[0]
	ans := nums[0]
	for _, num := range nums[1:] {
		if cur > 0 {
			cur = cur + num
		} else {
			cur = num
		}
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
