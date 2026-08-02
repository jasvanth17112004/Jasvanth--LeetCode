# I have tried with my logic but failed.soo Took a little bit of help.Jasvanth
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[0] * n for _ in range(n)]

        # If there is only one pile,
        # current player takes it.
        for i in range(n):
            dp[i][i] = piles[i]

        # Build for larger ranges
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                take_left = piles[i] - dp[i + 1][j]
                take_right = piles[j] - dp[i][j - 1]

                dp[i][j] = max(take_left, take_right)

        return dp[0][n - 1] > 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna