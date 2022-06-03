package problem46

func permute(nums []int) [][]int {
	ans := make([][]int, 0)
	n := len(nums)

	// 产生 nums[k:] 的所有排列
	var backtrack func(int)
	backtrack = func(pos int) {
		if pos == n {
			tmp := make([]int, n)
			copy(tmp, nums)
			ans = append(ans, tmp)
			return
		}

		for i := pos; i < n; i++ {
			nums[i], nums[pos] = nums[pos], nums[i]
			backtrack(pos + 1)
			nums[i], nums[pos] = nums[pos], nums[i]
		}
	}

	backtrack(0)
	return ans
}
