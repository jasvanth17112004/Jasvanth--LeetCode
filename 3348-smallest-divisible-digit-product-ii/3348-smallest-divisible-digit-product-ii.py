class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Factor t using only primes that can appear in digit products: 2, 3, 5, 7.
        x = t
        r2 = r3 = r5 = r7 = 0

        while x % 2 == 0:
            r2 += 1
            x //= 2
        while x % 3 == 0:
            r3 += 1
            x //= 3
        while x % 5 == 0:
            r5 += 1
            x //= 5
        while x % 7 == 0:
            r7 += 1
            x //= 7

        if x != 1:
            return "-1"

        # digit -> contribution to (2, 3, 5, 7)
        add2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        add3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        add5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        add7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        D2, D3, D5, D7 = r2 + 1, r3 + 1, r5 + 1, r7 + 1
        total = D2 * D3 * D5 * D7
        INF = 10 ** 9

        # dist[(a,b,c,d)] = minimum number of non-1 digits needed
        # to reach at least the required exponents (a,b,c,d).
        dist = [INF] * total
        dist[0] = 0

        max_sum = r2 + r3 + r5 + r7
        buckets = [[] for _ in range(max_sum + 1)]

        for a2 in range(D2):
            for a3 in range(D3):
                for a5 in range(D5):
                    for a7 in range(D7):
                        idx = (((a2 * D3 + a3) * D5 + a5) * D7 + a7)
                        buckets[a2 + a3 + a5 + a7].append(idx)

        for s in range(1, max_sum + 1):
            for idx_state in buckets[s]:
                x = idx_state
                a7 = x % D7
                x //= D7
                a5 = x % D5
                x //= D5
                a3 = x % D3
                a2 = x // D3

                best = INF

                for d in range(2, 10):
                    na2 = a2 - add2[d]
                    na3 = a3 - add3[d]
                    na5 = a5 - add5[d]
                    na7 = a7 - add7[d]

                    if na2 < 0:
                        na2 = 0
                    if na3 < 0:
                        na3 = 0
                    if na5 < 0:
                        na5 = 0
                    if na7 < 0:
                        na7 = 0

                    # Digit does not help at all.
                    if na2 == a2 and na3 == a3 and na5 == a5 and na7 == a7:
                        continue

                    nidx = (((na2 * D3 + na3) * D5 + na5) * D7 + na7)
                    best = min(best, dist[nidx] + 1)

                dist[idx_state] = best

        del buckets

        n = len(num)

        # Prefix product counts, capped at required exponents.
        pref2 = bytearray(n + 1)
        pref3 = bytearray(n + 1)
        pref5 = bytearray(n + 1)
        pref7 = bytearray(n + 1)

        for i, ch in enumerate(num):
            d = ord(ch) - 48

            v2 = pref2[i] + add2[d]
            v3 = pref3[i] + add3[d]
            v5 = pref5[i] + add5[d]
            v7 = pref7[i] + add7[d]

            if v2 > r2:
                v2 = r2
            if v3 > r3:
                v3 = r3
            if v5 > r5:
                v5 = r5
            if v7 > r7:
                v7 = r7

            pref2[i + 1] = v2
            pref3[i + 1] = v3
            pref5[i + 1] = v5
            pref7[i + 1] = v7

        first_zero = num.find('0')

        # If num itself is already valid.
        if first_zero == -1:
            if (pref2[n] == r2 and pref3[n] == r3 and
                pref5[n] == r5 and pref7[n] == r7):
                return num

        digit_str = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        def make_suffix(m: int, a2: int, a3: int, a5: int, a7: int) -> str:
            res = []
            rem2, rem3, rem5, rem7 = a2, a3, a5, a7

            for pos in range(m):
                rem_len = m - pos - 1

                for d in range(1, 10):
                    nr2 = rem2 - add2[d]
                    nr3 = rem3 - add3[d]
                    nr5 = rem5 - add5[d]
                    nr7 = rem7 - add7[d]

                    if nr2 < 0:
                        nr2 = 0
                    if nr3 < 0:
                        nr3 = 0
                    if nr5 < 0:
                        nr5 = 0
                    if nr7 < 0:
                        nr7 = 0

                    nidx = (((nr2 * D3 + nr3) * D5 + nr5) * D7 + nr7)

                    if dist[nidx] <= rem_len:
                        res.append(digit_str[d])
                        rem2, rem3, rem5, rem7 = nr2, nr3, nr5, nr7
                        break

            return "".join(res)

        # Try to keep the same length as num.
        upper = first_zero if first_zero != -1 else n - 1

        for p in range(upper, -1, -1):
            base = ord(num[p]) - 48
            if base == 9:
                continue

            m = n - p - 1

            for d in range(base + 1, 10):
                r2_rem = r2 - pref2[p] - add2[d]
                r3_rem = r3 - pref3[p] - add3[d]
                r5_rem = r5 - pref5[p] - add5[d]
                r7_rem = r7 - pref7[p] - add7[d]

                if r2_rem < 0:
                    r2_rem = 0
                if r3_rem < 0:
                    r3_rem = 0
                if r5_rem < 0:
                    r5_rem = 0
                if r7_rem < 0:
                    r7_rem = 0

                rem_idx = (((r2_rem * D3 + r3_rem) * D5 + r5_rem) * D7 + r7_rem)

                if dist[rem_idx] <= m:
                    suffix = make_suffix(m, r2_rem, r3_rem, r5_rem, r7_rem)
                    return num[:p] + digit_str[d] + suffix

        # Otherwise, use a longer length.
        need_idx = (((r2 * D3 + r3) * D5 + r5) * D7 + r7)
        L = max(n + 1, dist[need_idx])
        return make_suffix(L, r2, r3, r5, r7)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna