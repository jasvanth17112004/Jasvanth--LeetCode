//this Problem was solved by me . jasvanth
#include <stdlib.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int compare(const void* a, const void* b) {
    long long diff = *(long long*)a - *(long long*)b;
    if (diff < 0) return -1;
    if (diff > 0) return 1;
    return 0;
}

long long gcdSum(int* nums, int numsSize) {
    long long* prefixGcd = (long long*)malloc(numsSize * sizeof(long long));
    if (!prefixGcd) return 0;
    
    long long mx = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > mx) {
            mx = nums[i];
        }
        prefixGcd[i] = gcd((long long)nums[i], mx);
    }
    
    qsort(prefixGcd, numsSize, sizeof(long long), compare);
    

    long long total = 0;
    int left = 0, right = numsSize - 1;
    
    while (left < right) {
        total += gcd(prefixGcd[left], prefixGcd[right]);
        left++;
        right--;
    }
    
    
    free(prefixGcd);
    
    return total;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna