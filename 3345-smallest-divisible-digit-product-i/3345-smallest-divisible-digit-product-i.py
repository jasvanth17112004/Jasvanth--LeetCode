class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for i in range(n,101):
            if i<10:
                if i%t==0:
                    return i
                    break
            elif i==100:
                return i
            else:
                copy=i
                a,b=copy%10, copy//10
                print(b,a)
                if (a*b)%t==0:
                    return i
                    break
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna