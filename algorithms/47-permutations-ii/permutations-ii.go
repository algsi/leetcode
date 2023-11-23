package problem47

func permuteUnique(nums []int) [][]int {
	var ans [][]int
	n := len(nums)

	var backtrack func(int)
	backtrack = func(pos int) {
		if pos == n {
			tmp := make([]int, n)
			copy(tmp, nums)
			ans = append(ans, tmp)
			return
		}

		set := map[int]bool{}

		for i := pos; i < n; i++ {
			if ok, _ := set[nums[i]]; ok {
				continue
			}
			set[nums[i]] = true
			nums[i], nums[pos] = nums[pos], nums[i]
			backtrack(pos + 1)
			nums[i], nums[pos] = nums[pos], nums[i]
		}
	}
	backtrack(0)
	return ans
}
