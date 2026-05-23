class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        count = 0
        res = []

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
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, c in positions:
            if (r, c) in parent:
                res.append(count)
                continue
            
            parent[(r, c)] = (r, c)
            rank[(r, c)] = 1
            count += 1

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (nr, nc) in parent:
                    union((nr, nc), (r, c))
            
            res.append(count)
        
        return res