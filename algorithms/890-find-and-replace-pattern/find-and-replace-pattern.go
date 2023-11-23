package problem890

func findAndReplacePattern(words []string, pattern string) (ans []string) {
	for _, word := range words {
		if match(word, pattern) && match(pattern, word) {
			ans = append(ans, word)
		}
	}
	return
}

func match(word, pattern string) bool {
	mp := map[rune]byte{}
	for i, c := range word {
		y := pattern[i]
		if mp[c] == 0 {
			mp[c] = y
		} else if mp[c] != y {
			return false
		}
	}
	return true
}
