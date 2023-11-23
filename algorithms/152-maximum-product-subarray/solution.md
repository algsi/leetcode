# 最大连续子序列乘积

考虑存在负数的情况（PS：负负会得正），因此我们用两个辅助数组，`max[i]` 和 `min[i]`，`max[i]` 来表示以 `arr[i]` 结尾的最大连续子序列乘积，`min[i]` 来表示以 `arr[i]` 结尾的最小连续子序列乘积，因此状态转移方程为：

$$
min[i]=
\begin{cases}
 arr[0] & \text{if} \ i=0 \\
 min \{ arr[i], arr[i]*max[i-1], arr[i]*min[i-1] \} & \text{if} \ i>0 \\
\end{cases}
$$

和

$$
max[i]=
\begin{cases}
 arr[0] & \text{if} \ i=0 \\
 max \{ arr[i], arr[i]*max[i-1], arr[i]*min[i-1] \} & \text{if} \ i>0 \\
\end{cases}
$$

观察状态转移方程，我们其实只用到了前面的两个状态，所以我们可以用两个变量替代数组。
