//this is done by me.jasvanth.
#include <stdlib.h>

typedef struct {
    int value;
    int index;
} N;

int cmp(const void *a, const void *b) {
    N *x = (N *)a;
     N *y = (N *)b;

    if (x->value < y->value) return -1;
    if (x->value > y->value) return 1;
    return 0;
}

int* arrayRankTransform(int* arr, int arrSize, int* returnSize) {
    *returnSize = arrSize;

    if (arrSize == 0)
        return NULL;

    N *nodes = (N *)malloc(arrSize * sizeof(N));
    int *ans = (int *)malloc(arrSize * sizeof(int));

    for (int i = 0; i < arrSize; i++) {
        nodes[i].value = arr[i];
        nodes[i].index = i;
    }

    qsort(nodes, arrSize, sizeof(N), cmp);

    int rank = 1;
    ans[nodes[0].index] = rank;

    for (int i = 1; i < arrSize; i++) {
        if (nodes[i].value != nodes[i - 1].value)
            rank++;
        ans[nodes[i].index] = rank;
    }

    free(nodes);
    return ans;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna