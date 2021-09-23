package problem171

// titleToNumber 26进制
func titleToNumber(columnTitle string) int {
	if columnTitle == "" {
		return 0
	}
	tmp := 1
	ret := 0

	byteArr := []byte(columnTitle)
	base := int(byte('A'))
	for i := len(byteArr) - 1; i >= 0; i-- {
		ret += (int(byteArr[i]) - base + 1) * tmp
		tmp *= 26
	}

	return ret
}
