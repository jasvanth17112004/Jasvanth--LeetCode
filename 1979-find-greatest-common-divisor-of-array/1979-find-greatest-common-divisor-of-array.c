//this has been done by me.jasvanht
int findGCD(int* nums, int numsSize) {
    int smal = nums[0];
    int lar = nums[0];
    
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < smal) {
            smal = nums[i];
        }
        if (nums[i] > lar) {
            lar = nums[i];
        }
    }
    int a = smal;
    int b = lar;
    
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    
    return a;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna