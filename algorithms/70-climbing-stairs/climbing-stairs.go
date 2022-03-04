package problem70

// dynamic programming
// 当 n=1，f(1)=1
// 当 n=2，f(2)=2
// 当 n>2，f(n)=f(n-1)+f(n-2)
func climbStairs(n int) int {
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	f1, f2 := 1, 2
	for i := 3; i <= n; i++ {
		tmp := f2
		f2 = f1 + f2
		f1 = tmp
	}
	return f2
}
