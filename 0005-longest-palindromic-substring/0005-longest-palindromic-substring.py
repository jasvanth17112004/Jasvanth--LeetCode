class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        elif s==s[::-1]:
            return s
        l=0
        dummy=set()
        # print(s[0:2:+1],s[1::-1])
        for i in range(len(s)-1):
            # print(l)
            for j in range(l+1,len(s)+1):
                # print(l,j)
                # print(s[l:j],s[l:j][::-1] )
                if s[l:j]==s[l:j][::-1]:
                    dummy.add(s[l:j])
            l=l+1
        # print(dummy)
        if dummy:
            return max(dummy,key=len)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna