#this has been done by me with a lot of help.Jasvanth
from typing import List
from functools import lru_cache


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):

                opponent = dp(
                    i + X,
                    max(M, X)
                )

                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna