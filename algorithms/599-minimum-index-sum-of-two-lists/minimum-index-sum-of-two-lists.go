package problem599

import (
	"math"
)

func findRestaurant(list1 []string, list2 []string) []string {
	index := map[string]int{}
	ans := []string{}
	for i, v := range list1 {
		index[v] = i
	}

	indexSum := math.MaxInt64
	for i, v := range list2 {
		if j, ok := index[v]; ok {
			if i + j < indexSum {
				indexSum = i + j
				ans = []string{v}
			} else if i + j == indexSum {
				ans = append(ans, v)
			}
		}
	}
	return ans
}
