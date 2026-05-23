class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        count = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal count

            rootX, rootY = find(x), find(y)

            if rootX == rootY:
                return
            
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            
            count -= 1
        
        for i, v in edges:
            union(i, v)
        
        return count