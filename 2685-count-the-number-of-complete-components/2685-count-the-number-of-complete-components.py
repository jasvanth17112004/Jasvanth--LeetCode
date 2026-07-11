#this is done by me.jasvanth.no help
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n
        an = 0

        def dfs(node):
            visited[node] = True
            nodes.append(node)
            for nei in g[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i)

                v_count = len(nodes)
                e_count = 0

                for node in nodes:
                    e_count += len(g[node])

                e_count //= 2  

                if e_count == v_count * (v_count - 1) // 2:
                    an += 1

        return an

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna