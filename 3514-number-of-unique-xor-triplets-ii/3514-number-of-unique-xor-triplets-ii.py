#this has been done by me.jasvanth.
from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        max_val = max(nums)
        max_bit = max_val.bit_length()          
        size = 1 << max_bit                     


        pair_possible = [False] * size
        n = len(nums)
        for i in range(n):
            ni = nums[i]
            for j in range(n):
                pair_possible[ni ^ nums[j]] = True

        triplet_possible = [False] * size
        for x in range(size):
            if pair_possible[x]:
                for val in nums:
                    triplet_possible[x ^ val] = True

        return sum(triplet_possible)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna