package problem235

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// lowestCommonAncestorV1 利用二叉搜索树的特性做两次遍历，
func lowestCommonAncestorV1(root, p, q *TreeNode) *TreeNode {
	pathP := getPath(root, p)
	pathQ := getPath(root, q)
	var ancestor *TreeNode
	for i := 0; i < len(pathP) && i < len(pathQ) && pathP[i] == pathQ[i]; i++ {
		ancestor = pathP[i]
	}
	return ancestor
}

func getPath(node, target *TreeNode) []*TreeNode {
	var path []*TreeNode
	for node != nil {
		path = append(path, node)
		if node.Val == target.Val {
			return path
		}
		if node.Val > target.Val {
			node = node.Left
		} else {
			node = node.Right
		}
	}
	return path
}

// lowestCommonAncestorV2 一次遍历
func lowestCommonAncestorV2(root, p, q *TreeNode) *TreeNode {
	ancestor := root
	for {
		if p.Val < ancestor.Val && q.Val < ancestor.Val {
			ancestor = ancestor.Left
		} else if p.Val > ancestor.Val && q.Val > ancestor.Val {
			ancestor = ancestor.Right
		} else {
			return ancestor
		}
	}
}
