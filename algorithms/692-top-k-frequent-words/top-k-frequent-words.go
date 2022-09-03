package problem692

import (
	"container/heap"
	"sort"
)

// topKFrequent 哈希表 + 排序
func topKFrequent(words []string, k int) []string {
	cnt := make(map[string]int)
	for _, w := range words {
		cnt[w]++
	}
	uniqueWords := make([]string, 0, len(cnt))
	for w := range cnt {
		uniqueWords = append(uniqueWords, w)
	}
	sort.Slice(uniqueWords, func(i, j int) bool {
		s, t := uniqueWords[i], uniqueWords[j]
		return cnt[s] > cnt[t] || cnt[s] == cnt[t] && s < t
	})

	return uniqueWords[:k]
}

type pair struct {
	w string
	c int
}

// hp is a priority based on heap
// 定义优先队列底层数据结构
type hp []pair

func (h hp) Len() int {
	return len(h)
}

func (h hp) Less(i, j int) bool {
	a, b := h[i], h[j]
	return a.c < b.c || a.c == b.c && a.w > b.w
}

func (h hp) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *hp) Push(v interface{}) {
	*h = append(*h, v.(pair))
}

func (h *hp) Pop() interface{} {
	a := *h
	v := a[len(a)-1]
	*h = a[:len(a)-1]
	return v
}

// topKFrequentV2 优先队列
func topKFrequentV2(words []string, k int) []string {
	cnt := map[string]int{}
	for _, w := range words {
		cnt[w]++
	}
	h := &hp{}
	for w, c := range cnt {
		heap.Push(h, pair{w, c})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	ans := make([]string, k)
	for i := k - 1; i >= 0; i-- {
		ans[i] = heap.Pop(h).(pair).w
	}
	return ans
}
