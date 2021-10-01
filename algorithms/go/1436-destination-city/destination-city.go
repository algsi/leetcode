package problem1436

// destCity 哈希表
func destCity(paths [][]string) string {
	cityA := map[string]struct{}{}
	for _, path := range paths {
		cityA[path[0]] = struct{}{}
	}
	for _, path := range paths {
		if _, ok := cityA[path[1]]; !ok {
			return path[1]
		}
	}
	return ""
}
