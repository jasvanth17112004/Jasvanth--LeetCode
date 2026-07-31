#this is done by me.jasvanth.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0]==0:
            return [1]
        dummy=[]
        sum=0
        k=0
        for i in range(0,len(digits),+1):
            if digits[i]==0 and sum ==0:
                k=k+1
            else:
                sum=sum*10+digits[i]
        sum=sum+1
        sum=str(sum)
        sum=list(sum)
        m=k
        print(k,m)
        for i in range(0,len(sum)+k):
            if k!=0:
                dummy.append(0)
                print("he",i)
                k=k-1
            else:
                dummy.append(int(sum[i-m]))
                print(i)
        return dummy

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna