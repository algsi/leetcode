package problem53

// search binary search
func search(nums []int, target int) int {
	left := binarySearchLeft(nums, target)
	right := binarySearchRight(nums, target)
	return right - left
}

// binarySearchRight returns the index where to insert iterm x in list num, assuming num is sorted.
// The return value i is such that all e in nums[:i] have e < x, and all e in nums[i:] have e >= x.
func binarySearchLeft(nums []int, x int) int {
	lo := 0
	hi := len(nums)
	for lo < hi {
		mid := (lo + hi) / 2
		if nums[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

// binarySearchRight returns the index where to insert iterm x in list num, assuming num is sorted.
// The return value i is such that all e in a[:i] have e <= x, and all e in num[i:] have e > x.
func binarySearchRight(nums []int, x int) int {
	lo := 0
	hi := len(nums)
	for lo < hi {
		mid := (lo + hi) / 2
		if nums[mid] > x {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
