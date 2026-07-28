# this has been done by me.Jasvanth
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l= len(strs[0])
        index=0
        for i,v in enumerate(strs):
            if len(v)<l:
                l=len(v)
                index=i
        print(l,index)
        ref=strs[index]
        pre=""
        for i in range(len(ref)):
            ch=ref[i]
            for a in strs[::]:
                if ch!=a[i] :
                    return pre
            pre=pre+ch
        return pre

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna