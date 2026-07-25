class Solution:
    def maxProduct(self, n: int) -> int:
        val1,val2=sorted(str(n))[-2:len(str(n))]
        return int(val1)*int(val2)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna