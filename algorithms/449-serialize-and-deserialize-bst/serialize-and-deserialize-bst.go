package problem449

import (
	"math"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Codec 二叉搜索树编码
// 给定一棵二叉树的「先序遍历」和「中序遍历」可以恢复这颗二叉树。
// 给定一棵二叉树的「后序遍历」和「中序遍历」也可以恢复这颗二叉树。
// 而对于二叉搜索树，给定「先序遍历」或者「后序遍历」，对其经过排序即可得到「中序遍历」。
// 因此，仅对二叉搜索树做「先序遍历」或者「后序遍历」，即可达到序列化和反序列化的要求。
type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
// postorder
func (this *Codec) serialize(root *TreeNode) string {
	var arr []string
	var postOrder func(*TreeNode)
	postOrder = func(node *TreeNode) {
		if node == nil {
			return
		}
		postOrder(node.Left)
		postOrder(node.Right)
		arr = append(arr, strconv.Itoa(node.Val))
	}
	postOrder(root)
	return strings.Join(arr, " ")
}

// Deserializes your encoded data to tree.
// postorder
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	arr := strings.Split(data, " ")

	var constructor func(int, int) *TreeNode
	constructor = func(lower int, upper int) *TreeNode {
		if len(arr) == 0 {
			return nil
		}
		val, _ := strconv.Atoi(arr[len(arr)-1])
		if val < lower || val > upper {
			return nil
		}
		arr = arr[:len(arr)-1]
		return &TreeNode{
			Val:   val,
			Right: constructor(val, upper),
			Left:  constructor(lower, val),
		}
	}
	return constructor(math.MinInt32, math.MaxInt32)
}
