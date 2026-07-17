//this was done with help.Jasvanth
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gcdValues(int* nums, int numsSize, long long* queries, int queriesSize, int* returnSize) {
    // Find maximum value in nums
    int maxVal = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    
    // Count frequencies of each value
    long long* freq = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int i = 0; i < numsSize; i++) {
        freq[nums[i]]++;
    }
    
    // Count how many numbers are divisible by each value
    long long* divisibleCount = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int d = 1; d <= maxVal; d++) {
        long long count = 0;
        for (int multiple = d; multiple <= maxVal; multiple += d) {
            count += freq[multiple];
        }
        divisibleCount[d] = count;
    }
    
    // Calculate pairs with GCD exactly equal to each value
    long long* exactGCD = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int g = maxVal; g >= 1; g--) {
        long long totalPairs = divisibleCount[g] * (divisibleCount[g] - 1) / 2;
        // Subtract pairs with GCD > g (multiples of g)
        for (int multiple = 2 * g; multiple <= maxVal; multiple += g) {
            totalPairs -= exactGCD[multiple];
        }
        exactGCD[g] = totalPairs;
    }
    
    // Build prefix sums to answer queries
    long long* prefix = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int i = 1; i <= maxVal; i++) {
        prefix[i] = prefix[i - 1] + exactGCD[i];
    }
    
    // Answer queries
    int* answer = (int*)malloc(queriesSize * sizeof(int));
    *returnSize = queriesSize;
    
    for (int i = 0; i < queriesSize; i++) {
        long long q = queries[i];
        // Binary search to find the GCD value
        int left = 1, right = maxVal;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (prefix[mid] > q) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        answer[i] = left;
    }
    
    // Free allocated memory
    free(freq);
    free(divisibleCount);
    free(exactGCD);
    free(prefix);
    
    return answer;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna