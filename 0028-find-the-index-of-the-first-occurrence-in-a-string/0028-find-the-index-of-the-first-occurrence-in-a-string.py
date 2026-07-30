#this has been done by me .Jasvanth.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        for i,v  in enumerate(haystack):
            if v == needle[0]:
                if needle== haystack[i:i+l:+1]:
                    return i
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna