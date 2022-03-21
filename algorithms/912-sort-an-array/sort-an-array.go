package problem912

import (
	"math/rand"
)

// 快速排序
func sortArray(nums []int) []int {
	randomizedQuickSort(nums, 0, len(nums)-1)
	return nums
}

func randomizedQuickSort(nums []int, left, right int) {
	if right <= left {
		return
	}
	mid := randomizedPartition(nums, left, right)
	randomizedQuickSort(nums, left, mid-1)
	randomizedQuickSort(nums, mid+1, right)
}

func randomizedPartition(nums []int, left, right int) int {
	pivot := rand.Intn(right-left) + left // 区间中取随机数
	nums[pivot], nums[right] = nums[right], nums[pivot]
	i := left - 1
	for j := left; j < right; j++ {
		if nums[j] < nums[right] {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	i++
	nums[i], nums[right] = nums[right], nums[i]
	return i
}

// 归并排序
func sortArrayV2(nums []int) []int {
	mergeSort(nums, 0, len(nums)-1)
	return nums
}

// 合并
func mergeSort(nums []int, left, right int) {
	if right <= left {
		return
	}
	mid := (left + right) / 2
	mergeSort(nums, left, mid)
	mergeSort(nums, mid+1, right)
	var tmp []int
	i, j := left, mid+1
	for i <= mid || j <= right {
		if i > mid || (j <= right && nums[j] < nums[i]) {
			tmp = append(tmp, nums[j])
			j++
		} else {
			tmp = append(tmp, nums[i])
			i++
		}
	}

	copy(nums[left:right+1], tmp)
}
