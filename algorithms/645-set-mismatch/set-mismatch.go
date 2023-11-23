package problem645

// findErrorNumsV1 哈希表
func findErrorNumsV1(nums []int) []int {
	cnt := map[int]int{}
	for _, num := range nums {
		cnt[num]++
	}
	ans := make([]int, 2)
	for i := 1; i <= len(nums); i++ {
		if c := cnt[i]; c == 2 {
			ans[0] = i
		} else if c == 0 {
			ans[1] = i
		}
	}
	return ans
}

// findErrorNumsV2 数学法
func findErrorNumsV2(nums []int) []int {
	length := len(nums)
	total := sumDistinct(nums)
	ans := make([]int, 2)
	ans[0] = sum(nums) - total
	ans[1] = (1+length)*length/2 - total
	return ans
}

func sum(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}
	return res
}

func sumDistinct(nums []int) int {
	seen := map[int]bool{}
	res := 0
	for _, num := range nums {
		if ok := seen[num]; ok {
			continue
		} else {
			res += num
			seen[num] = true
		}
	}
	return res
}
