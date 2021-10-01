package package28

import "strings"

// strStrV1 暴力匹配
func strStrV1(haystack string, needle string) int {
	n, m := len(haystack), len(needle)

outer:
	for i := 0; i+m <= n; i++ {
		for j := range needle {
			if haystack[i+j] != needle[j] {
				continue outer
			}
		}
		return i
	}
	return -1
}

// strStrV2 使用语言特性
func strStrV2(haystack string, needle string) int {
	return strings.Index(haystack, needle)
}

// strStrV3 KMP算法
func strStrV3(haystack string, needle string) int {
	return 0
}
