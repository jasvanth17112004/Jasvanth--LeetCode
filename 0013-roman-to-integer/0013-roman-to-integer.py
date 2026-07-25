class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000 ,
            "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}        
        sum=0
        l=len(s)
        i=0
        while i<l:
            if i< l-1:
                if s[i:i+2] in dic:
                    sum=sum+dic[s[i:i+2]]
                    print(f"in {sum}")
                    i=i+1
                else:
                    sum=sum+dic[s[i]]
                    print(f"in2 {sum}")
            else:
                sum=sum+dic[s[i]]
                print(f"out {sum}")
            i=i+1
        return sum

                

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna