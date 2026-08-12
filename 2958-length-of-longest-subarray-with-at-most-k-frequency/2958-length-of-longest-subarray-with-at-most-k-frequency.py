#this has been done by me.Jasvanth.
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        left=0
        res=0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while freq[nums[right]]>k:
                freq[nums[left]] -= 1
                left+= 1
            res = max(res,right-left+1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna