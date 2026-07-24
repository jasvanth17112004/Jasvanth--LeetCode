class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,value in enumerate(nums):
            comp=target-value
            if comp in seen:
                return [seen[comp],i]
            seen[value]=i
        return[]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna