package problem944

func minDeletionSize(strs []string) int {
	output := 0
	row := len(strs)
	col := len(strs[0])
	for j := 0; j < col; j++ {
		for i := 1; i < row; i++ {
			if strs[i-1][j] > strs[i][j] {
				output++
				break
			}
		}
	}
	return output
}
