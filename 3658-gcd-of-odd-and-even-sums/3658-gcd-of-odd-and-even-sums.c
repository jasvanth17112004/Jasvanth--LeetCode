//This is all done by me.jasvanth.Thank you.
int gcdOfOddEvenSums(int n) {
    int sumodd=0;
    int sumeven=0;
    int gcd=0;
    for(int i=1;i<n+1;i++)
    {
        sumeven=sumeven+(i*2);
        sumodd=sumodd+((i*2)-1);  

    }
    for(int i=1;i<=sumodd/2+1;i++)
    {
        if(sumodd%i==0 && sumeven%i==0)
        {
            gcd=i;
        }
        else{
            continue;
        }
    }

    return gcd;

}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna