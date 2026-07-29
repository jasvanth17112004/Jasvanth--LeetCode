#This has been done nby jasvanth with a lot of help.
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        half = [x // 2 for x in cnt]
        L = sum(half)  

        fact = [1] * (L + 1)
        for i in range(1, L + 1):
            fact[i] = fact[i - 1] * i

        denom = 1
        for x in half:
            denom *= fact[x]

        total = fact[L] // denom

        if k > total:
            return ""

        center = s[n // 2] if n % 2 else ""

        left = []

        for pos in range(L):
            rem = L - pos

            for i in range(26):
                if half[i] == 0:
                    continue

                ways = total * half[i] // rem

                if k > ways:
                    k -= ways
                else:
                    left.append(chr(ord('a') + i))
                    total = ways
                    half[i] -= 1
                    break

        left_str = "".join(left)
        return left_str + center + left_str[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna