#this has been done by me.Jasvanth.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if " " not in s:
            return len(s)
        a=list(s)
        i=len(a)-1
        while a[i]==" ":
            if a[i]==" ":
                a.pop()
                i=i-1
        if " " not in a:
            return len(a)
        k=0
        l=len(a)-1
        dummy=[]
        while a[l]!=" ":
            if a[l]!=" ":
                dummy.append(a[l])
                l=l-1
        return len(dummy)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna