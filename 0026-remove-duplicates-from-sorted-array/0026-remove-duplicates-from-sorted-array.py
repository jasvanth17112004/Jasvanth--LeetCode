class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[k-1] != nums[i]:
                nums[k]=nums[i]
                k=k+1  
        return k          



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna