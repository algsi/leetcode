package problem82

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	dummyHead := &ListNode{}
	dummyHead.Next = head

	prev := dummyHead
	cur := head
	for cur != nil && cur.Next != nil {
		if cur.Val == cur.Next.Val {
			tmp := cur.Next.Next
			for tmp != nil && tmp.Val == cur.Val {
				tmp = tmp.Next
			}
			prev.Next = tmp
			cur = tmp
		} else {
			prev = cur
			cur = cur.Next
		}
	}

	return dummyHead.Next
}
