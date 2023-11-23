package problem284

type Iterator struct{}

func (it *Iterator) hasNext() bool {
	// Returns true if the iteration has more elements.
	return false
}

func (it *Iterator) next() int {
	// Returns the next element in the iteration.
	return 0
}

type PeekingIterator struct {
	iter        *Iterator
	hashNext    bool
	nextElement int
}

// Constructor 构造 PeekingIterator 迭代器
func Constructor(iter *Iterator) *PeekingIterator {
	return &PeekingIterator{
		iter:        iter,
		hashNext:    iter.hasNext(),
		nextElement: iter.next(),
	}
}

func (it *PeekingIterator) hasNext() bool {
	return it.hashNext
}

func (it *PeekingIterator) next() int {
	ret := it.nextElement
	it.hashNext = it.iter.hasNext()
	if it.hashNext {
		it.nextElement = it.iter.next()
	}
	return ret
}

func (it *PeekingIterator) peek() int {
	return it.nextElement
}
