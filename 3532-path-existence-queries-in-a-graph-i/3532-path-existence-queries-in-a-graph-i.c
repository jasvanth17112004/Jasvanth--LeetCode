//this is done by me .jasvanth.
#include <stdlib.h>
#include <stdbool.h>

bool* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff, int** queries, int queriesSize,int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;

    bool *a = (bool *)malloc(sizeof(bool) * queriesSize);

    int *compo = (int *)malloc(sizeof(int) * n);

    compo[0] = 0;
    int comp = 0;

    for (int i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] <= maxDiff)
            compo[i] = comp;
        else
            compo[i] = ++comp;
    }

    for (int i = 0; i < queriesSize; i++) {
        int u = queries[i][0];
        int v = queries[i][1];
        a[i] = (compo[u] == compo[v]);
    }

    free(compo);
    return a;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna