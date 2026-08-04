#this has been done by me .Jasvanth.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        enc=set()
        left=0
        for right in range(len(s)):
            while s[right] in enc:
                enc.remove(s[left])
                left=left+1
            enc.add(s[right])
            result=max(result,right-left+1)
        return result

                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna