package problem930

// numSubArraysWithSumV1 哈希表 + 前缀和
// 时间复杂度：O(n)
// 空间复杂度：O(n)
func numSubArraysWithSumV1(nums []int, goal int) int {
	sum := 0
	prefixSumMap := make(map[int]int) // 前缀和 map
	ans := 0
	for _, num := range nums {
		prefixSumMap[sum]++
		sum += num
		ans += prefixSumMap[sum-goal]
	}

	return ans
}
