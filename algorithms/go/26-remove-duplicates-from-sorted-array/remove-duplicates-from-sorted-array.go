package package26

// removeDuplicates dual pointer(快慢指针)
func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	n := len(nums)
	fast, slow := 1, 1
	for fast < n {
		if nums[fast] != nums[fast-1] {
			nums[slow] = nums[fast]
			slow++
		}
		fast++
	}
	return slow
}
