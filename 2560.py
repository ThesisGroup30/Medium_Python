class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = max(dp[i - 1][1], nums[i - 1])
            for j in range(2, min(i, k) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + nums[i - 1])

        return dp[n][k]
