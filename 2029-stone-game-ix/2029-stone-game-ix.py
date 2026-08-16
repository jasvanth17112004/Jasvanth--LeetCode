#this was done with help.Sorry fot today.Jasvanth.
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0,c1,c2=0,0,0
        for x in stones:
            if x%3==0:
                c0=c0+1
            elif x%3== 1:
                c1=c1+1
            else:
                c2+=1
        if c0%2== 0:
            return c1>0 and c2>0
        else:
            return abs(c1-c2)>2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna