#this has been done by me.Jasvanth.
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)%2==0:
            a=sorted(s[:len(s)//2])
            return "".join(a+a[::-1])     
        else:
            a=s[:len(s)//2]
            b=[s[len(s)//2]]
            a=sorted(a)
            return "".join(a+b+a[::-1])






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna