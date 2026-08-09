class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            sum1=width*h
            water=max(water,sum1)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return water


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna