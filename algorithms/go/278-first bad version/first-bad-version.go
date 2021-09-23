package problem278

// binary search
func firstBadVersion(n int) int {
	lo, hi := 0, n
	for lo < hi {
		var mid = (hi-lo)/2 + lo
		if isBadVersion(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return hi
}

func isBadVersion(version int) bool {
	return true
}
