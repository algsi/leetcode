// package problem215
package main

// 快速排序算法
func findKthLargest(nums []int, k int) int {
	n := len(nums)
	left, right := 0, n-1
	if left == right {
		return nums[left]
	}
	piv := partition(nums, left, right)
	for k != piv+1 {
		if k > piv+1 {
			left = piv + 1
		} else {
			right = piv - 1
		}

		if left == right {
			return nums[left]
		}
		piv = partition(nums, left, right)
	}

	return nums[piv]
}

// slice partition in reverse order
func partition(nums []int, left, right int) int {
	// select a pivot
	pivot := left
	nums[pivot], nums[right] = nums[right], nums[pivot]
	i := left - 1
	for j := left; j < right; j++ {
		// reverse order
		if nums[j] > nums[right] {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	i++
	nums[i], nums[right] = nums[right], nums[i]
	return i
}
