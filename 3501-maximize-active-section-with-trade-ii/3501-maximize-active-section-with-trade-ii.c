#include <stdlib.h>
#include <string.h>

int* maxActiveSectionsAfterTrade(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = strlen(s);
    
    // ---------- Compress into runs ----------
    int* run_len = (int*)malloc(n * sizeof(int));
    int* run_type = (int*)malloc(n * sizeof(int));
    int* run_start = (int*)malloc(n * sizeof(int));
    int* pos_to_run = (int*)malloc(n * sizeof(int));
    int m = 0, total1 = 0, i = 0;
    
    while (i < n) {
        int j = i;
        char c = s[i];
        while (j < n && s[j] == c) j++;
        run_type[m] = c - '0';
        run_len[m] = j - i;
        run_start[m] = i;
        if (c == '1') total1 += run_len[m];
        for (int k = i; k < j; k++) pos_to_run[k] = m;
        m++;
        i = j;
    }
    
    // ---------- Extract 0-run lengths ----------
    int K = 0;
    for (int idx = 0; idx < m; idx++)
        if (run_type[idx] == 0) K++;
    
    int* zero_len = NULL;
    int* run_to_zero = NULL;
    int* A = NULL;
    int** st = NULL;
    int* logs = NULL;
    int A_len = 0, max_j = 0;
    
    if (K > 0) {
        zero_len = (int*)malloc(K * sizeof(int));
        run_to_zero = (int*)malloc(m * sizeof(int));
        for (int idx = 0; idx < m; idx++) run_to_zero[idx] = -1;
        int z = 0;
        for (int idx = 0; idx < m; idx++) {
            if (run_type[idx] == 0) {
                run_to_zero[idx] = z;
                zero_len[z] = run_len[idx];
                z++;
            }
        }
        
        if (K >= 2) {
            A_len = K - 1;
            A = (int*)malloc(A_len * sizeof(int));
            for (int idx = 0; idx < A_len; idx++)
                A[idx] = zero_len[idx] + zero_len[idx + 1];
            
            // Sparse table for range max query on A
            logs = (int*)malloc((A_len + 1) * sizeof(int));
            logs[0] = 0;  // safe fallback
            logs[1] = 0;
            for (int idx = 2; idx <= A_len; idx++)
                logs[idx] = logs[idx / 2] + 1;
            max_j = logs[A_len];
            st = (int**)calloc(max_j + 1, sizeof(int*));
            st[0] = (int*)malloc(A_len * sizeof(int));
            memcpy(st[0], A, A_len * sizeof(int));
            for (int j = 1; j <= max_j; j++) {
                int prev_len = A_len - (1 << j) + 1;
                st[j] = (int*)malloc(prev_len * sizeof(int));
                for (int idx = 0; idx < prev_len; idx++) {
                    int a = st[j - 1][idx];
                    int b = st[j - 1][idx + (1 << (j - 1))];
                    st[j][idx] = (a > b) ? a : b;
                }
            }
        }
    }
    
    // ---------- Answer queries ----------
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int l = queries[q][0], r = queries[q][1];
        int i_l = pos_to_run[l], i_r = pos_to_run[r];
        int offset_l = l - run_start[i_l], offset_r = r - run_start[i_r];
        
        int first_0 = -1, last_0 = -1;
        if (run_type[i_l] == 0) {
            first_0 = i_l;
        } else if (i_l + 1 < m && run_start[i_l + 1] <= r) {
            first_0 = i_l + 1;
        }
        if (run_type[i_r] == 0) {
            last_0 = i_r;
        } else if (i_r - 1 >= 0 && run_start[i_r] - 1 >= l) {
            last_0 = i_r - 1;
        }
        
        int gain = 0;
        if (first_0 != -1 && last_0 != -1 && first_0 <= last_0) {
            int z_left = run_to_zero[first_0];
            int z_right = run_to_zero[last_0];
            if (z_right > z_left) {
                int trunc_left, trunc_right;
                if (run_type[i_l] == 0)
                    trunc_left = run_len[i_l] - offset_l;
                else
                    trunc_left = run_len[first_0];
                if (run_type[i_r] == 0)
                    trunc_right = offset_r + 1;
                else
                    trunc_right = run_len[last_0];
                
                int cand1 = trunc_left + ((z_left + 1 == z_right) ? trunc_right : zero_len[z_left + 1]);
                int cand2 = ((z_right - 1 == z_left) ? trunc_left : zero_len[z_right - 1]) + trunc_right;
                gain = (cand1 > cand2) ? cand1 : cand2;
                
                // Internal fully-enclosed pairs exist only when there are at least two internal zero runs.
                if (z_right - z_left >= 3) {
                    int l_in = z_left + 1, r_in = z_right - 2;
                    int len = r_in - l_in + 1;
                    int j = logs[len];
                    int a = st[j][l_in];
                    int b = st[j][r_in - (1 << j) + 1];
                    int internal = (a > b) ? a : b;
                    if (internal > gain) gain = internal;
                }
            }
        }
        ans[q] = total1 + gain;
    }
    
    // ---------- Free memory ----------
    free(run_len); free(run_type); free(run_start); free(pos_to_run);
    if (zero_len) free(zero_len);
    if (run_to_zero) free(run_to_zero);
    if (A) free(A);
    if (st) {
        for (int j = 0; j <= max_j; j++) free(st[j]);
        free(st);
    }
    if (logs) free(logs);
    
    *returnSize = queriesSize;
    return ans;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna