package problem138

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

var cacheNode map[*Node]*Node

func deepCopy(node *Node) *Node {
	if node == nil {
		return nil
	}
	if n, ok := cacheNode[node]; ok {
		return n
	}
	newNode := &Node{Val: node.Val}
	cacheNode[node] = newNode

	// 递归拷贝
	newNode.Next = deepCopy(node.Next)
	newNode.Random = deepCopy(node.Random)
	return newNode
}

// copyRandomListV1 哈希表 + 回溯
func copyRandomListV1(head *Node) *Node {
	cacheNode = map[*Node]*Node{}
	return deepCopy(head)
}

// copyRandomListV2 迭代 + 节点拆分
func copyRandomListV2(head *Node) *Node {

	return nil
}
