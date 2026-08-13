#this was totally done by help.jasvanth.
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        size = 4 * n

        # tree[node] = [left_char, right_char, length, prefix, suffix, best]
        tree = [None] * size

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc = a[0]
            rc = b[1]
            length = a[2] + b[2]

            prefix = a[3]
            suffix = b[4]
            best = max(a[5], b[5])

            if a[1] == b[0]:
                best = max(best, a[4] + b[3])

                if a[3] == a[2]:
                    prefix = a[2] + b[3]

                if b[4] == b[2]:
                    suffix = b[2] + a[4]

            return [lc, rc, length, prefix, suffix, best]

        def build(node, left, right):
            if left == right:
                tree[node] = [s[left], s[left], 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, idx, char):
            if left == right:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, right, idx, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][5])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna