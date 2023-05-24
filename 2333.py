class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        dp = [[float('inf')] * (k2 + 1) for _ in range(k1 + 1)]
        dp[0][0] = 0

        for i in range(k1 + 1):
            for j in range(k2 + 1):
                for x in range(1, n + 1):
                    diff = (nums1[x - 1] - nums2[x - 1]) ** 2

                    if i >= 1:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + diff)

                    if j >= 1:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + diff)

        return dp[k1][k2]
