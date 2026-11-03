from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        visited=[0]*n
        graph=[[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(visited,graph,node):
            q=deque([node])
            visited[node]=1
            while q:
                cnode=q.popleft()
                for nbr in graph[cnode]:
                    if not visited[nbr]:
                        q.append(nbr)
                        visited[nbr]=1
        bfs(visited,graph,source)
        if visited[destination]:
            return True
        else:
            return False


        