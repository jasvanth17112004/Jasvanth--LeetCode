#this is done by me.jasvanth.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==2:
            return 1
        if x==0:
            return 0
        
        for i in range(0,x):
            if i*i>x:
                return i-1
                break
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna