class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
        
        emailToName = {}

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 1
                emailToName[email] = name
        
        for account in accounts:
            firstEmail = account[1]
            for email in account[2:]:
                union(firstEmail, email)
        
        res = []
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)
        
        for root, email in groups.items():
            name = emailToName[root]
            res.append([name] + sorted(email))
        
        return res
