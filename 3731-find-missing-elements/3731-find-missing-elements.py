#this has been done by me.jasvanth.
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        dummy=[]
        for i in range(nums[0],nums[-1],+1):
            if i not in nums:
                dummy.append(i)
        return dummy

            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna