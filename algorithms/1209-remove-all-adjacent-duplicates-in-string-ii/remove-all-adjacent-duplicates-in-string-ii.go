package problem1209

type pair struct {
	cnt int
	ch  rune
}

func removeDuplicates(s string, k int) string {
	var stack []*pair
	for _, ch := range s {
		if len(stack) == 0 || ch != stack[len(stack)-1].ch {
			stack = append(stack, &pair{1, ch})
		} else {
			top := stack[len(stack)-1]
			top.cnt++
			if top.cnt == k {
				stack = stack[:len(stack)-1]
			}
		}
	}

	// reverse
	var chars []rune
	for i := 0; i < len(stack); i++ {
		for j := 0; j < stack[i].cnt; j++ {
			chars = append(chars, stack[i].ch)
		}
	}

	return string(chars)
}
