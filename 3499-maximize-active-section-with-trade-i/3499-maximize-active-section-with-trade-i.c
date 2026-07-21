//This has been totally done with help.had to take help since i was travelling and tired.Jasvanth.

#include <stdlib.h>
#include <string.h>

int maxActiveSectionsAfterTrade(char* s) {
    int n = strlen(s);
    int m = n + 2;

    char *t = (char*)malloc((size_t)m + 1);
    t[0] = '1';
    memcpy(t + 1, s, n);
    t[m - 1] = '1';
    t[m] = '\0';

    long long originalOnes = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') originalOnes++;
    }

    // Run-length encode t
    int *runLen = (int*)malloc(sizeof(int) * m);
    char *runChar = (char*)malloc((size_t)m);
    int numRuns = 0;

    int i = 0;
    while (i < m) {
        int j = i;
        while (j < m && t[j] == t[i]) j++;
        runChar[numRuns] = t[i];
        runLen[numRuns] = j - i;
        numRuns++;
        i = j;
    }

    long long bestGain = 0;
    // interior 1-runs are those with index strictly between 0 and numRuns-1
    for (int k = 1; k < numRuns - 1; k++) {
        if (runChar[k] == '1') {
            long long gain = (long long)runLen[k - 1] + (long long)runLen[k + 1];
            if (gain > bestGain) bestGain = gain;
        }
    }

    long long answer = originalOnes + bestGain;

    free(t);
    free(runLen);
    free(runChar);

    return (int)answer;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna