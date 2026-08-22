#this is done by me.jasvanth.
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        product=1
        copy=n
        while n !=0:
            a=n%10
            sum=sum+a
            product=product*a
            n=n//10
        return copy % (sum+product)==0

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna