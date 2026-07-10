#this is done by jasvanth with a lot of help 
from typing import List
import bisect

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort indices by value
        order = sorted(range(n), key=lambda i: nums[i])
        sortedVals = [nums[i] for i in order]
        pos = [0] * n
        for sp, orig in enumerate(order):
            pos[orig] = sp

        # Two-pointer: next[i] = farthest sorted position reachable directly from i
        next_arr = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and sortedVals[j+1] - sortedVals[i] <= maxDiff:
                j += 1
            next_arr[i] = j

        # Binary lifting table
        LOG = max(1, (n).bit_length() + 1)
        up = [next_arr[:]]
        for k in range(1, LOG):
            prev = up[-1]
            cur = [prev[prev[i]] for i in range(n)]
            up.append(cur)

        def min_hops(lo, hi):
            if lo >= hi:
                return 0
            current = lo
            hops = 0
            for k in reversed(range(LOG)):
                nxt = up[k][current]
                if nxt < hi:
                    hops += (1 << k)
                    current = nxt
            # one more single hop needed
            final = next_arr[current]
            if final == current:
                return -1
            hops += 1
            if final < hi:
                return -1  # shouldn't happen if LOG sufficient; safety net
            return hops

        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
            a, b = pos[u], pos[v]
            lo, hi = min(a, b), max(a, b)
            answer.append(min_hops(lo, hi))

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna