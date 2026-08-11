#this has been done b y me.Jasvanth
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]+1
        sum=nums[0]
        b=True
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                print(i)
                sum=sum+nums[i]
            else:
                break
        while sum in nums:
            sum=sum+1
        else:
            return sum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna