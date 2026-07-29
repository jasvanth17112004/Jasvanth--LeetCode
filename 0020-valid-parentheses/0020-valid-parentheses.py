#this has been done by me. jasvanth.
class Solution:
    def isValid(self, s: str) -> bool:
        op = ["(", "{", "["]
        cl = [")", "}", "]"]

        stack = []

        for i in s:
            if i in op:
                stack.append(i)

            elif stack:
                if cl.index(i) == op.index(stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna