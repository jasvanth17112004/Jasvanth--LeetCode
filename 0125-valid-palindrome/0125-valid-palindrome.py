#this has been done by me.jasvanth
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        dum=[]
        for i,v in enumerate(a):
            if (ord(v)>=ord("a") and ord(v)<=ord("z")) or ord(v)>=ord("0") and ord(v)<=ord("9"):
                dum.append(v)
        dum="".join(dum)
        return dum==dum[::-1]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna