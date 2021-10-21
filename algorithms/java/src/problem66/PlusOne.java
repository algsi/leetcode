package problem66;

/**
 * @author Xavier Li
 */
public class PlusOne {

    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            // 找出从末尾数第一个不为 9 的数字
            if (digits[i] != 9) {
                digits[i]++;
                for (int j = i + 1; j < n; j++) {
                    digits[j] = 0;
                }
                return digits;
            }
        }
        // 全都是 9
        int[] ans = new int[n + 1];
        ans[0] = 1;
        return ans;
    }

}
