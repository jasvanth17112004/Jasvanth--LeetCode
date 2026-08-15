class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=0
        for num in nums:
            x=x^num
        if x!=0:
            return len(nums)
        for num in nums:
            if num !=0:
                return len(nums)-1
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna