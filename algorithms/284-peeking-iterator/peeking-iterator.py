class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        self._next = iterator.next()
        self._has_next = iterator.hasNext()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        ret = self._next
        self._has_next = self._iter.hasNext()
        if self._has_next:
            self._next = self._iter.next()
        else:
            self._next = 0
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next
