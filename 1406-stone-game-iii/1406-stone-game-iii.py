#this has been done by me with a lot of help.jasvanth
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        # dp[i] = maximum score difference
        # current player can achieve starting from i
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            total = 0
            dp[i] = float("-inf")

            # Take 1, 2, or 3 stones
            for j in range(i, min(i + 3, n)):

                total += stoneValue[j]

                # My score - opponent's best advantage
                dp[i] = max(dp[i], total - dp[j + 1])

        if dp[0] > 0:
            return "Alice"

        elif dp[0] < 0:
            return "Bob"

        else:
            return "Tie"


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna