package problem1221

func balancedStringSplit(s string) int {
	var ans = 0
	d := 0
	for _, ch := range s {
		if ch == 'L' {
			d++
		} else {
			d--
		}
		if d == 0 {
			ans++
		}
	}
	return ans
}
