#this has been done by me.Jasvanth.
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        a = Counter(word)
        b = sorted(a.values(), reverse=True)
        # print(b)
        p = 0
        for i, v in enumerate(b):
            sum = i // 8 + 1
            p += v * sum

        return p

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna