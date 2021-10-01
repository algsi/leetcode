package problem326;

/**
 * Problem 326: power of three
 * <p>3的幂
 */
public class Solution {
    public boolean isPowerOfThree(int n) {
        while (n != 0 && n % 3 == 0) {
            n = n / 3;
        }
        return n == 1;
    }
}
