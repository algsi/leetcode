package problem128

// longestConsecutive 哈希表
func longestConsecutive(nums []int) int {
	numSet := make(map[int]struct{})
	for _, n := range nums {
		numSet[n] = struct{}{}
	}

	ret := 0
	for n := range numSet {
		if _, ok := numSet[n-1]; !ok {
			seqCount := 1
			for ; ; seqCount++ {
				if _, ok := numSet[n+seqCount]; ok {
					continue
				}
				break
			}
			if seqCount > ret {
				ret = seqCount
			}
		}
	}

	return ret
}
