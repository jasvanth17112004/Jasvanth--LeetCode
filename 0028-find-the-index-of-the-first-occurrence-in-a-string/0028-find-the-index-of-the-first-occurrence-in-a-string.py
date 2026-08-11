#this has been done by me .Jasvanth.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        k=0
        for i in range(len(needle),len(haystack)+1):
            if needle!=haystack[k:i]:
                k=k+1
            else:
                return k
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna