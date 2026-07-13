//half of the work is mine here and other half was done with help.jasvanth.
#include <stdlib.h>

int* sequentialDigits(int low, int high, int* returnSize) {
    int *ans = (int *)malloc(40 * sizeof(int));
    *returnSize = 0;

    char digits[] = "123456789";

    //Length of sequential number
    for (int len = 2; len <= 9; len++) {
        //Starting pos
        for (int start = 0; start + len <= 9; start++) {
            int num = 0;
            for (int i = start; i < start + len; i++) {
                num = num * 10 + (digits[i] - '0');
            }

            if (num >= low && num <= high) {
                ans[(*returnSize)++] = num;
            }
        }
    }

    return ans;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna