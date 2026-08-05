#this has been done by me.Jasvanth
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)
        suspicious = set()
        stack = [k]
        while stack:
            method = stack.pop()

            if method in suspicious:
                continue
            suspicious.add(method)
            for next_method in graph[method]:
                stack.append(next_method)
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna