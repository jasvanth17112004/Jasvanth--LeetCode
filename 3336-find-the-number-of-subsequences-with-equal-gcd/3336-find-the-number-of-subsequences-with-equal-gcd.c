//most of it was done with help.i had to present myself somewhere else.
#include <stdlib.h>
#include <string.h>

#define MAXV 200
#define MOD 1000000007

static int gcd(int a,int b){
    while(b){
        int t=a%b;
        a=b;
        b=t;
    }
    return a;
}

int subsequencePairCount(int* nums, int numsSize) {

    static long long dp[MAXV+1][MAXV+1];
    static long long ndp[MAXV+1][MAXV+1];

    memset(dp,0,sizeof(dp));
    dp[0][0]=1;

    for(int idx=0;idx<numsSize;idx++){

        memset(ndp,0,sizeof(ndp));

        int x=nums[idx];

        for(int g1=0;g1<=MAXV;g1++){

            for(int g2=0;g2<=MAXV;g2++){

                long long cur=dp[g1][g2];

                if(cur==0) continue;

                /* ignore */
                ndp[g1][g2]=(ndp[g1][g2]+cur)%MOD;

                /* put into seq1 */

                int ng1=(g1==0)?x:gcd(g1,x);

                ndp[ng1][g2]+=cur;
                if(ndp[ng1][g2]>=MOD) ndp[ng1][g2]-=MOD;

                /* put into seq2 */

                int ng2=(g2==0)?x:gcd(g2,x);

                ndp[g1][ng2]+=cur;
                if(ndp[g1][ng2]>=MOD) ndp[g1][ng2]-=MOD;
            }
        }

        memcpy(dp,ndp,sizeof(dp));
    }

    long long ans=0;

    for(int g=1;g<=MAXV;g++){

        ans+=dp[g][g];

        ans%=MOD;
    }

    return (int)ans;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna