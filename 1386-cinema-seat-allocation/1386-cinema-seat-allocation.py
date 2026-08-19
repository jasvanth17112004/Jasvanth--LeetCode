#this wasnt done by me.jasvanth.(unable to use my brain)
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Store reserved seats for only the rows that actually have reservations.
        rows = {}

        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # Every completely free row can accommodate 2 groups.
        ans = 2 * n

        # Bitmasks for the three possible blocks.
        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            # This row was initially counted as 2 groups.
            # Find how many groups it can actually accommodate.

            if (mask & left) == 0 and (mask & right) == 0:
                # Both left and right blocks are free.
                # They don't overlap, so 2 groups.
                continue

            if (mask & left) == 0 or (mask & middle) == 0 or (mask & right) == 0:
                # At least one valid block exists.
                ans -= 1
            else:
                # No block is available.
                ans -= 2

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna