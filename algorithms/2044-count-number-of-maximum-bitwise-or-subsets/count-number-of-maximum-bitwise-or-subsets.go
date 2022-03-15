package problem2044


func countMaxOrSubsets(nums []int) int {
	maxOr, cnt := 0, 0

	var dfs func(pos int, orVal int)
	dfs = func(pos int, orVal int) {
		if pos == len(nums) {
			if orVal > maxOr {
				maxOr = orVal
				cnt = 1
			} else if orVal == maxOr {
				cnt++
			}
			return
		}

		dfs(pos + 1, orVal)
		dfs(pos + 1, orVal | nums[pos])
	}

	dfs(0, 0)
	return cnt
}
