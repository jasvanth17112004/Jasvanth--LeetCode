#this has been done by me .Jasvanth.
class Solution:
    def minimumPushes(self, word: str) -> int:
            pushes = 0
            for i in range(len(word)):
                if i < 8:
                    pushes += 1
                elif 8 <= i <= 15:
                    pushes += 2
                elif 16 <= i <= 23:
                    pushes += 3
                else:
                    pushes += 4
            return pushes
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna