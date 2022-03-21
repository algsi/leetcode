package problem148


type ListNode struct {
    Val int
    Next *ListNode
}

// 自顶向下归并排序
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	// cut the linked list at the mid index
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// cut the linkage
    mid := slow.Next
    slow.Next = nil
	left, right := sortList(head), sortList(mid)	
	return merge(left, right)
}

// 自底向上归并排序
func sortListV2(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	length := 0
	node := head
	for node != nil {
		length++
		node = node.Next
	}

	dummyHead := &ListNode{}
	dummyHead.Next = head
	subLen := 1

	for subLen < length {
		prev := dummyHead
		cur := prev.Next

		for cur != nil {
			// first sub list
			head1 := cur
			i := 1
			for i < subLen && cur.Next != nil {
				cur = cur.Next
				i++
			}

			// second sub list
			head2 := cur.Next
			cur.Next = nil // cur the linkage
			i = 1
			cur = head2
			for i < subLen && cur != nil && cur.Next != nil {
				cur = cur.Next
				i++
			}

			// save the next head
			var nextHead *ListNode
			if cur != nil {
				nextHead = cur.Next
				cur.Next = nil
			}

			// merge and reconnect
			prev.Next = merge(head1, head2)
			for prev.Next != nil {
				prev = prev.Next
			}
			
			cur = nextHead
		}

		subLen <<= 1
	}

	return dummyHead.Next
}

func merge(head1 *ListNode, head2 *ListNode) *ListNode {
	dummy_h := &ListNode{}
	h := dummy_h
	for head1 != nil && head2 != nil {
		if head1.Val < head2.Val {
			h.Next = head1
			head1 = head1.Next
		} else {
			h.Next = head2
			head2 = head2.Next
		}
		h = h.Next
	}
	if head1 != nil {
		h.Next = head1
	} else if head2 != nil {
		h.Next = head2
	}

	return dummy_h.Next
}
