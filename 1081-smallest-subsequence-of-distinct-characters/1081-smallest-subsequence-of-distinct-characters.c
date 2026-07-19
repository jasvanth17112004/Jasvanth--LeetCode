//The problem has been solved by me.Thank you
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* smallestSubsequence(char* s) {
    int len = strlen(s);
    int lastPos[26];
    for (int i = 0; i < 26; i++) {
        lastPos[i] = -1;
    }
    for (int i = 0; i < len; i++) {
        lastPos[s[i] - 'a'] = i;
    }
    
    bool inStack[26] = {false};
    char* stack = (char*)malloc((len + 1) * sizeof(char));
    int top = -1;
    
    for (int i = 0; i < len; i++) {
        char c = s[i];
        int idx = c - 'a';
        if (inStack[idx]) {
            continue;
        }
        while (top >= 0 && stack[top] > c && lastPos[stack[top] - 'a'] > i) {
            inStack[stack[top] - 'a'] = false;
            top--;
        }
        stack[++top] = c;
        inStack[idx] = true;
    }
    
    stack[top + 1] = '\0';
    return stack;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna