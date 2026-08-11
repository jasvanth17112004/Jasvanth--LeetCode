#this has been done by me.Jasvanth
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        count=0
        for k in range(1,len(nums),+1):
            if nums[i]!=nums[k]:
                nums[i+1]=nums[k]
                i=i+1
                count=i

        return count+1





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna