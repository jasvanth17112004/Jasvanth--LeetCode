//this is done by me.jasvanth. with lot of help with overflow-
#include <string.h>
#include <stdlib.h>

int* sumAndMultiply(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;
    int* result = (int*)malloc(queriesSize * sizeof(int));
    if (result == NULL) return NULL; 
    
    long long MOD = 1000000007;
    int m = strlen(s);
    int* prefixSum = (int*)malloc((m + 1) * sizeof(int));
    prefixSum[0] = 0;
    for (int i = 0; i < m; i++) {
        prefixSum[i + 1] = prefixSum[i] + (s[i] - '0');
    }

    int* nz_idx = (int*)malloc(m * sizeof(int)); 
    int nz_count = 0;
    for (int i = 0; i < m; i++) {
        if (s[i] != '0') {
            nz_idx[i] = nz_count++;
        } else {
            nz_idx[i] = -1;
        }
    }
    int* next_nz = (int*)malloc(m * sizeof(int));
    int* prev_nz = (int*)malloc(m * sizeof(int));
    int last = -1;
    for (int i = m - 1; i >= 0; i--) {
        if (s[i] != '0') last = nz_idx[i];
        next_nz[i] = last;
    }
    last = -1;
    for (int i = 0; i < m; i++) {
        if (s[i] != '0') last = nz_idx[i];
        prev_nz[i] = last;
    }
    long long* power10 = (long long*)malloc((nz_count + 1) * sizeof(long long));
    long long* prefixVal = (long long*)malloc((nz_count + 1) * sizeof(long long));
    power10[0] = 1;
    prefixVal[0] = 0;
    
    int nz_curr = 0;
    for (int i = 0; i < m; i++) {
        if (s[i] != '0') {
            power10[nz_curr + 1] = (power10[nz_curr] * 10) % MOD;
            prefixVal[nz_curr + 1] = (prefixVal[nz_curr] * 10 + (s[i] - '0')) % MOD;
            nz_curr++;
        }
    }

    for(int i = 0; i < queriesSize; i++)
    {
        int start = queries[i][0];
        int end = queries[i][1];
        
        long long sum = (prefixSum[end + 1] - prefixSum[start]) % MOD;
        long long copy = 0; 
        
        int L = next_nz[start];
        int R = prev_nz[end];
        
        if (L != -1 && R != -1 && L <= R) {
            int len = R - L + 1;
            copy = (prefixVal[R + 1] - (prefixVal[L] * power10[len]) % MOD + MOD) % MOD;
        }

        long long use = copy; 
        result[i] = (int)((use * sum) % MOD);
    }
    
    free(prefixSum); 
    free(nz_idx);
    free(next_nz);
    free(prev_nz);
    free(power10);
    free(prefixVal);
    
    return result;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna