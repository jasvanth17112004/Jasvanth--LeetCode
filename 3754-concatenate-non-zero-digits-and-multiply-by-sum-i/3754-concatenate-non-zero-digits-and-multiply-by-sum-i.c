//This is done by me. #jasvanth.
long long sumAndMultiply(int n) {
    long long copy=n;
    long x=0;
    for(int i=0;copy!=0;i++)
    {
        if(copy%10>0)
        {
            x=x*10+copy%10;
            copy=copy/10;
        }  
        else
        {
            copy=copy/10;
        } 
        
    }
    copy=x;
    x=0;
    long sum=0;
    for(int i=0;copy!=0;i++)
    {
            x=x*10+copy%10;
            sum=sum+copy%10;
            copy=copy/10;   
    }
    long long final=x*sum;

    return final;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna