//this has been done by me with a lot of help.jasvanth
#include <stdlib.h>

int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;
    
    k = k % total;
    if (k == 0) {
        int** result = (int**)malloc(m * sizeof(int*));
        *returnColumnSizes = (int*)malloc(m * sizeof(int));
        for (int i = 0; i < m; i++) {
            result[i] = (int*)malloc(n * sizeof(int));
            (*returnColumnSizes)[i] = n;
            for (int j = 0; j < n; j++) {
                result[i][j] = grid[i][j];
            }
        }
        *returnSize = m;
        return result;
    }
    int* flat = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            flat[i * n + j] = grid[i][j];
        }
    }
    
    int* shifted = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < total; i++) {
        int newPos = (i + k) % total;
        shifted[newPos] = flat[i];
    }

    int** result = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) {
        result[i] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[i] = n;
        for (int j = 0; j < n; j++) {
            result[i][j] = shifted[i * n + j];
        }
    }
    
    free(flat);
    free(shifted);
    *returnSize = m;
    return result;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna