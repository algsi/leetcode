package problem92

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	dummyHead := &ListNode{}
	dummyHead.Next = head

	// find left
	pre := dummyHead
	for i := 0; i < left-1; i++ {
		pre = pre.Next
	}
	leftNode := pre.Next

	// find right
	rightNode := pre
	for i := 0; i < right-left+1; i++ {
		rightNode = rightNode.Next
	}

	// cut
	cur := rightNode.Next
	pre.Next = nil
	rightNode.Next = nil

	reverseList(leftNode)
	pre.Next = rightNode
	leftNode.Next = cur

	return dummyHead.Next
}

func reverseList(head *ListNode) {
	var prev *ListNode
	cur := head
	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
}
